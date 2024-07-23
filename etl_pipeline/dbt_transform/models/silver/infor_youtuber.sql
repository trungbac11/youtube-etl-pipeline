select
    youtuber,
    subscribers,
    video_views,
    uploads,
    country,
    channel_type
from {{ ref('raw_information') }}