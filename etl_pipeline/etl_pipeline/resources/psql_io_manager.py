from contextlib import contextmanager
from sqlalchemy import create_engine
import pandas as pd
from dagster import IOManager, InputContext, OutputContext
from datetime import datetime
import psycopg2
from psycopg2 import sql
import psycopg2.extras

@contextmanager
def connect_psql(config):
    conn_info = (
        f"postgresql+psycopg2://{config['user']}:{config['password']}"
        + f"@{config['host']}:{config['port']}"
        + f"/{config['database']}"
    )
    engine = create_engine(conn_info)
    connection = engine.raw_connection()
    try:
        yield connection
    finally:
        connection.close()

class PostgreSQLIOManager(IOManager):
    def __init__(self, config):
        self._config = config
    
    def load_input(self, context: InputContext) -> pd.DataFrame:
        pass
    
    def handle_output(self, context: "OutputContext", obj: pd.DataFrame):
        schema = context.asset_key.path[-2]
        table = str(context.asset_key.path[-1]).replace("warehouse_", "")
        context.log.debug(f"Schema: {schema}, Table: {table}")
        tmp_tbl = f"{table}_tmp_{datetime.now().strftime('%Y_%m_%d')}"
        try:
            with connect_psql(self._config) as conn:
                context.log.debug(f"Connected to PostgreSQL: {conn}")
                primary_keys = (context.metadata or {}).get("primary_keys", [])
                context.log.debug(f"Primary keys: {primary_keys}")

                with conn.cursor() as cursor:
                    context.log.debug(f"Cursor info: {cursor}")
                    cursor.execute("SELECT version()")
                    context.log.info(f"PostgreSQL version: {cursor.fetchone()}")
                    
                    # Create temp table
                    cursor.execute(
                        f"CREATE TEMP TABLE IF NOT EXISTS {tmp_tbl} (LIKE {schema}.{table})"
                    )
                    cursor.execute(f"SELECT COUNT(*) FROM {tmp_tbl}")
                    context.log.debug(
                        f"Log for creating temp table: {cursor.fetchone()}"
                    )
                    
                    # Create SQL identifiers for the column names
                    columns = sql.SQL(",").join(
                        sql.Identifier(name.lower()) for name in obj.columns
                    )
                    
                    # Create a placeholder for the values
                    values = sql.SQL(",").join(sql.Placeholder() for _ in obj.columns)
                    
                    # Create the insert query
                    context.log.debug("Inserting data into temp table")
                    insert_query = sql.SQL("INSERT INTO {} ({}) VALUES({});").format(
                        sql.Identifier(tmp_tbl), columns, values
                    )
                    
                    # Execute the insert query
                    psycopg2.extras.execute_batch(cursor, insert_query, obj.values)
                    conn.commit()

                    # Check data inserted
                    context.log.debug("Checking data inserted")
                    cursor.execute(f"SELECT COUNT(*) FROM {tmp_tbl};")
                    context.log.info(f"Number of rows inserted: {cursor.fetchone()}")

                    # Upsert data
                    if len(primary_keys) > 0:
                        context.log.debug("Table has primary keys, upserting data")
                        conditions = " AND ".join(
                            [
                                f""" {schema}.{table}."{k}" = {tmp_tbl}."{k}" """
                                for k in primary_keys
                            ]
                        )
                        command = f"""
                            BEGIN;
                            DELETE FROM {schema}.{table}
                            USING {tmp_tbl}
                            WHERE {conditions};

                            INSERT INTO {schema}.{table}
                            SELECT * FROM {tmp_tbl};

                            COMMIT;
                        """
                    else:
                        context.log.debug("Table has no primary keys, replacing data")
                        command = f"""
                            BEGIN;
                            DELETE FROM {schema}.{table};

                            INSERT INTO {schema}.{table}
                            SELECT * FROM {tmp_tbl};

                            COMMIT;
                        """

                    context.log.debug(f"Upserting data into {schema}.{table}")
                    cursor.execute(command)
                    context.log.debug(f"{cursor.statusmessage}")
                    conn.commit()
        except Exception as e:
            context.log.error(f"Error while handling output to PostgreSQL: {e}")

        try:
            with connect_psql(self._config) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(f"SELECT COUNT(*) FROM {schema}.{table};")
                    context.log.info(
                        f"Number of rows upserted in {schema}.{table}: {cursor.fetchone()}"
                    )

                    # Drop temp table
                    cursor.execute(f"DROP TABLE {tmp_tbl}")
                    conn.commit()
        except Exception as e:
            context.log.error(f"Error while testing handle_output to PostgreSQL: {e}")