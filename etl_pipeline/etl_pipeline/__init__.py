from dagster import Definitions, load_assets_from_modules
from dagster import load_assets_from_modules, file_relative_path
from dagster_dbt import dbt_cli_resource
from dagster_dbt import load_assets_from_dbt_project

import os
from . import assets
from .resources.mysql_io_manager import MySQLIOManager
from .resources.minio_io_manager import MinIOIOManager
from .resources.psql_io_manager import PostgreSQLIOManager


MYSQL_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "database": "youtube_channels",
    "user": "admin",
    "password": "admin123",
}

MINIO_CONFIG = {
    "endpoint_url": "localhost:9000",
    "bucket": "warehouse",
    "aws_access_key_id": "minio",
    "aws_secret_access_key": "minio123",
}


PSQL_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "postgres",
    "user": "admin",
    "password": "admin123",
}

DBT_PROJECT_PATH = file_relative_path(__file__, "../dbt_transform")
DBT_PROFILES = file_relative_path(__file__, "../dbt_transform")

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH,
    profiles_dir=DBT_PROFILES,
    key_prefix=["dbt"],
)

all_assets = load_assets_from_modules([assets]) + dbt_assets
resources = {
    "mysql_io_manager": MySQLIOManager(MYSQL_CONFIG),
    "minio_io_manager": MinIOIOManager(MINIO_CONFIG),
    "psql_io_manager": PostgreSQLIOManager(PSQL_CONFIG),
    "dbt": dbt_cli_resource.configured(
        {
            "project_dir": DBT_PROJECT_PATH,
            "profiles_dir": DBT_PROFILES,
        }
    ),
}

defs = Definitions(
    assets=all_assets,
    resources=resources
)
