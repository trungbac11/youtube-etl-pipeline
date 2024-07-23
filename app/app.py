import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Page title
st.set_page_config(page_title='YouTube Search app', page_icon='📊')
st.title('📊 YouTube Search app')

# App description - Explain functionalities in an expander box
with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app shows the use of Pandas for df wrangling, Altair for chart creation and editable dfframe for df interaction.')
  st.markdown('**How to use the app?**')
  st.warning('To engage with the app, 1. Select genres of your interest in the drop-down selection box and then 2. Select the year duration from the slider widget. As a result, this should generate an updated editable dfFrame and line plot.')
  

# Load df - Read CSV into a Pandas dfFrame
df = pd.read_csv('/home/tranbac1128/YOUTUBE_ETL_PIPELINE/youtube_channels/youtube_information.csv')

# Application Title
# st.header('YouTube Search app Dashboard')

# Sidebar Filters
st.sidebar.header('Filter Options')
selected_category = st.sidebar.selectbox('Category', options=df['category'].dropna().unique(), index=0)
selected_country = st.sidebar.selectbox('Country', options=df['country'].dropna().unique(), index=0)
selected_channel_type = st.sidebar.selectbox('Channel Type', options=df['channel_type'].dropna().unique(), index=0)

# Filter df
filtered_df = df[
    (df['category'] == selected_category) &
    (df['country'] == selected_country) &
    (df['channel_type'] == selected_channel_type)
]

# Overview Section
st.header('Overview')
st.write(filtered_df.describe())

# Detailed Channel Information
st.header('Channel Information')
selected_channel = st.selectbox('Select a Channel', options=filtered_df['youtuber'])
channel_df = filtered_df[filtered_df['youtuber'] == selected_channel].iloc[0]

st.write(f"**Youtuber:** {channel_df['youtuber']}")
st.write(f"**Subscribers:** {channel_df['subscribers']}")
st.write(f"**Video Views:** {channel_df['video_views']}")
st.write(f"**Uploads:** {channel_df['uploads']}")
st.write(f"**Category:** {channel_df['category']}")
st.write(f"**Country:** {channel_df['country']}")
st.write(f"**Channel Type:** {channel_df['channel_type']}")
