-- Drop the database if it exists and create a new one
DROP DATABASE IF EXISTS youtube_channels;
CREATE DATABASE youtube_channels;
USE youtube_channels;

-- Drop the table if it exists and create a new one for movies
DROP TABLE IF EXISTS youtube_information;
CREATE TABLE youtube_information(
    channels_rank INT primary key,
    youtuber VARCHAR(255),
    subscribers BIGINT,
    video_views BIGINT,
    category VARCHAR(255),
    title VARCHAR(255),
    uploads INT,
    country VARCHAR(255),
    abbreviation VARCHAR(10),
    channel_type VARCHAR(50),
    video_views_rank INT,
    country_rank INT,
    channel_type_rank INT,
    video_views_for_the_last_30_days INT,
    lowest_monthly_earnings BIGINT,
    highest_monthly_earnings BIGINT,
    lowest_yearly_earnings BIGINT,
    highest_yearly_earnings BIGINT,
    subscribers_for_last_30_days BIGINT,
    created_year INT,
    created_month VARCHAR(10),
    created_date INT,
    gross_tertiary_education_enrollment DECIMAL(5, 2),
    population BIGINT,
    unemployment_rate DECIMAL(5, 2),
    urban_population BIGINT,
    latitude DECIMAL(10, 6),
    longitude DECIMAL(10, 6)
);
