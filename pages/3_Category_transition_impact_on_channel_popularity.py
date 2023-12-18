import streamlit as st
import pandas as pd
from utils.ploting import *
import os

# Emoji list: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/ 
st.set_option('deprecation.showPyplotGlobalUse', False)

st.write(
    """
    Hi! Small demo of our tool to explore Youtube channels. Enjoy :100:
    """
)

@st.cache_data 
def load_data(channels_path, helper_path):
    df_channels = pd.read_csv(channels_path)
    df_channels.sort_values(by='name_cc', inplace=True)
    return df_channels, pd.read_feather(helper_path)

def channel_id_from_channel_name(channel_name):
    channel_id = df_channels[df_channels['name_cc'] == channel_name]['channel']
    return list(channel_id)[0]

LOCAL_PATH = os.getcwd()
df_channels, df_helper = load_data(os.path.join(LOCAL_PATH, 'Data/People_&_Blogs/df_PB_channels.csv'),  os.path.join(LOCAL_PATH, 'Data/People_&_Blogs/df_PB_helper.feather'))

default_channel_index = df_channels['name_cc'].unique().tolist().index("The LaBrant Fam")
channel_name = st.selectbox(
    ':red[Select a YouTube Channel] :popcorn:',
    df_channels['name_cc'].unique(),
    index = default_channel_index
)
channel_id = channel_id_from_channel_name(channel_name)

time_range = pd.period_range(start=pd.to_datetime("2015-01"), end=pd.to_datetime("2019-10"), freq='M')
time_range_str = time_range.strftime('%Y-%m').tolist()  # Convert the periods to strings for display in the selectbox
time_range_str_desc = time_range.sort_values(ascending=False).strftime('%Y-%m').tolist()
default_start_date_index = time_range_str.index("2016-09")
default_end_date_index = time_range_str_desc.index("2019-09")
default_transition_date_index = time_range_str.index("2018-02")
start_date_str = st.selectbox(
    'Select the start of the time window :soon:',
    time_range_str,
    index = default_start_date_index
)
end_date_str = st.selectbox(
    'Select the end of the time window :end:',
    time_range_str_desc,
    index=default_end_date_index
)
transition_date_str = st.selectbox(
    'Select a date that marks the transition of category',
    time_range_str, 
    index = default_transition_date_index,
    disabled = False
)

if channel_id:

    df_helper_id = df_helper[df_helper['channel_id'] == channel_id]

    visualize_evolution_of_channel(channel_id, df_helper_id, channel_name, start_date_str, end_date_str, transition_date_str)
    video_likes_and_views(channel_id, df_helper_id, channel_name, start_date_str, end_date_str, transition_date_str)
    video_frequency_and_duration(channel_id, df_helper_id, channel_name, start_date_str, end_date_str, transition_date_str)
    
    # If using Plotly, you might return the figure from the function and use st.plotly_chart()
    # fig = visualize_evolution_of_channel(channel_id, df_feather, channels_df)
    # st.plotly_chart(fig)