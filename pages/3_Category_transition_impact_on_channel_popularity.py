import streamlit as st
import pandas as pd
from utils.ploting import visualize_evolution_of_channel, \
    video_likes_and_views, video_frequency_and_duration
import os

# Emoji list: http://tinyurl.com/streamlit-emojis
st.set_option('deprecation.showPyplotGlobalUse', False)
easter_eggs = {
    "TED": "You look like a man of deep culture",
    "Lady Gaga": "Rah, rah-ah-ah-ah, Roma, roma-ma, Gaga, ooh-la-la, Want your\
          bad romance"
}
st.write(
    """
    Hi! Here is a small demo of our tool to explore Youtube channels. \
        Enjoy :100:

    By default the analysis is done on "The LaBrant Fam" channel,\
        which started with funny videos before shifting to vlogging\
        their family life.
    They today have 13m subscribers, with all of their videos surpassing\
        500k views. \

    However, don't hesitate to use the tools to explore the evolution of your\
        favorite blogging channel (we have hidden some easter eggs).
    Some example of famous channels are TED, Lady Gaga...
    """
)


@st.cache_data
def load_data(channels_path, helper_path):
    df_channels = pd.read_csv(channels_path, compression='infer')
    df_channels.sort_values(by='name_cc', inplace=True)
    return df_channels, pd.read_feather(helper_path)


def channel_id_from_channel_name(channel_name):
    channel_id = df_channels[df_channels['name_cc'] == channel_name]['channel']
    return list(channel_id)[0]


LOCAL_PATH = os.getcwd()
WEB_DATA = os.path.join(LOCAL_PATH, 'website_data')
PEOPLE_BLOGS_PATH = os.path.join(WEB_DATA, 'People_&_Blogs')
TOP_1000_PATH = os.path.join(PEOPLE_BLOGS_PATH, 'top_1000')

df_channels, df_helper = load_data(os.path.join(TOP_1000_PATH,
                                                'df_top_1000_channels.csv.gz'),
                                   os.path.join(TOP_1000_PATH,
                                                'df_top_1000_helper.feather'))

default_channel_index = df_channels['name_cc'].unique()\
                                            .tolist()\
                                            .index("The LaBrant Fam")
channel_name = st.selectbox(
    ':red[Select a YouTube Channel] :popcorn:',
    df_channels['name_cc'].unique(),
    index=default_channel_index
)
channel_id = channel_id_from_channel_name(channel_name)

time_range = pd.period_range(start=pd.to_datetime("2015-01"),
                             end=pd.to_datetime("2019-10"), freq='M')
# Convert the periods to strings for display in the selectbox
time_range_str = time_range.strftime('%Y-%m').tolist()
time_range_str_desc = time_range.sort_values(ascending=False)\
                                .strftime('%Y-%m').tolist()
default_start_date_index = time_range_str.index("2016-09")
default_end_date_index = time_range_str_desc.index("2019-09")
default_transition_date_index = time_range_str.index("2018-02")
start_date_str = st.selectbox(
    'Select the start of the time window :soon:',
    time_range_str,
    index=default_start_date_index
)
end_date_str = st.selectbox(
    'Select the end of the time window :end:',
    time_range_str_desc,
    index=default_end_date_index
)
transition_date_str = st.selectbox(
    'Select a date that marks the transition of category',
    time_range_str,
    index=None,
    disabled=False
)

if channel_name:

    df_helper_id = df_helper[df_helper['channel_id'] == channel_id]

    visualize_evolution_of_channel(channel_id,
                                   df_helper_id,
                                   channel_name,
                                   start_date_str,
                                   end_date_str,
                                   transition_date_str)
    video_likes_and_views(channel_id,
                          df_helper_id,
                          channel_name,
                          start_date_str,
                          end_date_str,
                          transition_date_str)
    video_frequency_and_duration(channel_id,
                                 df_helper_id,
                                 channel_name,
                                 start_date_str,
                                 end_date_str,
                                 transition_date_str)

    # If using Plotly, you might return the figure from the function
    # and use st.plotly_chart()
    # fig = visualize_evolution_of_channel(channel_id, df_feather, channels_df)
    # st.plotly_chart(fig)

    st.write("""## Analysis of channel evolution:""")

    if channel_name == "The LaBrant Fam":
        st.write("""
                Analysis of The LaBrant Fam
                 """)
    elif channel_name in easter_eggs.keys():
        st.write(easter_eggs[channel_name])
    else:
        st.write("Did you think we had that much free time to explore every\
                  channel? Try another one!")
