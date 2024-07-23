import pandas as pd
from dagster import asset, Output, Definitions, AssetIn, multi_asset, AssetOut
from dagster import file_relative_path
from dagster_dbt import load_assets_from_dbt_project

@asset(
    io_manager_key="minio_io_manager",
    required_resource_keys={"mysql_io_manager"},
    key_prefix=["bronze", "youtube"],
    compute_kind="MySQL"
)
def bronze_youtube_information(context) -> Output[pd.DataFrame]:
    sql_stm = "SELECT * FROM youtube_information"
    pd_data = context.resources.mysql_io_manager.extract_data(sql_stm)
    
    return Output(
        pd_data,
        metadata={
            "table": "youtube_information",
            "records count": len(pd_data),
        },
    )

@multi_asset(
    ins={
        "bronze_youtube_information": AssetIn(key_prefix=["bronze", "youtube"])
    },
    outs={
        "youtube_information": AssetOut(
            io_manager_key="psql_io_manager",
            key_prefix=["warehouse", "public"],
            metadata={
                "primary_keys": [
                    "channels_rank"
                ],
                "columns": [
                    "channels_rank",
                    "youtuber",
                    "subscribers",
                    "video_views",
                    "category",
                    "title",
                    "uploads",
                    "country",
                    "abbreviation",
                    "channel_type",
                    "countrycode",
                    "continent",
                    "videos_gained",
                    "videos_lost",
                    "videos_deleted",
                    "subscribers_gained",
                    "subscribers_lost",
                    "subscribers_for_last_30_days",
                    "created_year",
                    "created_month",
                    "created_date",
                    "gross_tertiary_education_enrollment",
                    "population",
                    "unemployment_rate",
                    "urban_population",
                    "latitude",
                    "longitude"
                ]
            },
        )
    },
    compute_kind="PostgreSQL"
)
def youtube_information(bronze_youtube_information) -> Output[pd.DataFrame]:
    return Output(
        bronze_youtube_information,
        metadata={
            "schema": "public",
            "table": "youtube_information",
            "records count": len(bronze_youtube_information),
        },
    )
    