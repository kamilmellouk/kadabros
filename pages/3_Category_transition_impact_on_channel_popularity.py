import streamlit as st
import pandas as pd
from utils.inteteractive_plotting import visualize_evolution_of_channel, \
    video_frequency_and_duration, video_likes_and_views
import os

# Emoji list: http://tinyurl.com/streamlit-emojis

easter_eggs = {
    "TED": "You look like a man of deep culture",
    "Lady Gaga": "Rah, rah-ah-ah-ah, Roma, roma-ma, Gaga, ooh-la-la, Want your\
          bad romance",
    "CaseyNeistat": "Did you see his last video? It's crazy isn't it?!",
    "123GO!": "Are you sure you are not too old for that?",
    "Jake Paul": "Is he more a boxer or a youtuber now?",
    "1 Million Creation": "Best youtube channel : https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "WhispersRed ASMR": "Are you lost too?"
}

st.header("Category transition impact analysis")
st.write(
    """
    By default the charts are showing the data of "The LaBrant Fam" channel,\
        which started off with funny videos before shifting to vlogging\
        their family life. The suburban familly originally from California have now move to Tennessee, and is very close to their community.
    They today have 13m subscribers, with all of their videos surpassing\
        1 million views. \
    """
)
st.write(
    """
    We are giving you access to our exploration tools over the channels. 
    We filtered the channels to keep only the top 1000 channels of the People & Blogs category (ranked by number of subscribers).
    Check out your favorite YouTube channel, like Ted :books:, Casey Neistat :sunglasses: or Lady Gaga :notes:. We even prepared some easter eggs for you! :gift: 
    Go also check other interessing transitionning channels like BUzzFeedVideo.
    """
) # Go also check other interessing transitionning channels like Joey Graceffa and ???.


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
    ':violet[Select a YouTube Channel] :popcorn:',
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
default_start_date_index = time_range_str.index("2015-01")
default_end_date_index = time_range_str_desc.index("2019-10")
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
    'Select a date that marks the transition of category :clipboard:',
    time_range_str,
    index=None,
    disabled=False
)

df_helper_id = df_helper[df_helper['channel_id'] == channel_id]

if channel_name == "The LaBrant Fam":

    
    transition_date = "2018-01"

    st.subheader("The LaBrant Family evolution")
    st.write("""Analyzing the following charts, we observe the evolution of a YouTube channel, here showcasing the dynamics of the LaBrant family account over time. We will focus on their transition from comedy to vlogging in January 2018, as well as the changes in video characteristics before and after this shift.""")
    
    st.write("""#### 1. Category Shift Impact: """)
    visualize_evolution_of_channel(df_helper_id,
                                   channel_name,
                                   start_date_str,
                                   end_date_str,
                                   transition_date)
    st.write("""This first chart indicates a pivotal change in January 2018, where the predominant video category first move from Comedy to People & Blogs. 
             By looking more into details at the YouTube channel, we notice that the new content direction took place before the switch of the videos categories, around July 2017""")
    st.write("""
             Indeed, Cole, the father, first gained popularity on the social media Vine. 
             He then met his wife Savannah at 19 years old and transitioned over to YouTube. 
             They began with funny skits, in line with their Vine videos. 
             **Before the transition**, the chart shows a consitent presence on the plateform, with a monthly upload average of 8 videos. 
             This can result from a organized production schedule. 
             The year 2016 symbolizes a period where the first YouTube creators began living off their content's earnings.
             You can still look at their YouTube channel to see them (for those not deleted) : `FAMILY BAKING PRANK WAR`, `DRIVING WITH CIKE | MCDONALDS ROMANCE?!` and `BLINDFOLD TASTE CHALLENGE WITH 3 YEAR OLD!!`.
             """)
    st.write("""         
             **After the transition**, there's a significant increase in video production. The number of vlogs rises sharply and stabilizes at a higher level than the comedy videos (around 13 by month).
             Vlogging allows for more spontaneous content creation and potentially less production and preparation time compared to funnier videos, which might explain the increased output.
             The consistency and frequency of uploading suggests a strategic decision to engage more frequently with the audience. 
             It allows to build a more personal connection with a channel's viewerbase. 
             The transition might also reveal a will to produce something more in line with their family life and values.
             Some example of videos uploaded in 2019 are `our Vegas trip did not go as planned` and `We Caught Everleigh Lying To Us...`.
             We see that videos titles also align with the genre transitioning, going from uppercase to lowercase, more realistic for their fans.
             """)

    st.write("""#### 2. Video Characteristics Evolution:""")   
    video_likes_and_views(df_helper_id,
                          channel_name,
                          start_date_str,
                          end_date_str,
                          transition_date)
    st.write("""The second chart provides insights into the like-to-view ratio, with larger markers indicating months with higher view counts.
             This ratio serves as a useful metric for gauging the positive impact a video has on viewers during its viewing.""")
    st.write("""
             **Before the transition**, the like-to-view ratio was varied before July 2016, with some months achieving ratios over 3.5%, likely due to specific comedy videos resonating with the audience.
             Between July 2016 and the transition defined in January 2018, the impact of the videos on the comunity stabilizes at a low level, around 1%.
             We can also see bigger markers, which means more views during this pre-transition period. 
             For example, the wedding video uploaded in July 2017 cumulates today over 50 millions of views. 
             This shows that their content was reaching a wider viewership than after the transition.
             """)
    st.write("""    
             **After transitioning**, it appears that the like-to-view ratio experiences a slight upward trend, but the number of views is decreasing compared to early buzz. 
             The loyal fan base remains, albeit less populated, finding greater enjoyment in videos that showcase the intimate aspects of family life. 
             Viewers are becoming more connected to each member of the family, as they see the kids growing.
             """)

    st.write("""#### 3. Video Duration and Production Volume:""")
    video_frequency_and_duration(df_helper_id,
                                 start_date_str,
                                 end_date_str,
                                 transition_date)
    st.write("""The third chart shows both the mean video duration and the count of videos per month. 
             There's a clear upward trend in video duration over time, indicating that the channel's videos became longer on average, which is common in vlogging content as it tends to cover daily life events that require longer footage and less cuts.""")
    st.write("""
    **Before the transition**, the video duration varied but stayed within a lower range of less than 10 minutes. 
             This is typical for comedy content, which tends to be shorter to be attractive.
             The ceiling of video duration at 10 minutes starting from the end of 2017 also corresponds to the double advertising before the video if it's longer than 10 minutes, which pushed video lengths across all categories.  
    """)
    st.write("""
    **After the transition,** not only did the number of videos increase, but the average duration also did. 
             This suggests a strategic choice to provide more in-depth content about the intimate life of Cole, Savannah, and their childs. 
             The steady increase in video length could also reflect the channel's confidence in retaining viewer attention for longer periods, a sign of a maturing content strategy and growing audience engagement.
    """)

    st.write("""#### Analysis Synopsis""")
    st.write("""
    The transition from comedy to vlogging has had a significant impact on "The LaBrant Fam" channel. The shift led to increased video output and longer content, which aligns with the more personal and confessional strategy of the family. 
             The increase in the like-to-view ratio post-transition suggests that the audience received the new content direction positively. 
             Overall, the transition appears to have been successful for our favorite family, with the channel adapting its content to meet audience preferences and possibly to align with broader trends in viewer engagement on YouTube.
    """)

else: 

    visualize_evolution_of_channel(df_helper_id,
                                   channel_name,
                                   start_date_str,
                                   end_date_str,
                                   transition_date_str)
    video_likes_and_views(df_helper_id,
                          channel_name,
                          start_date_str,
                          end_date_str,
                          transition_date_str)
    video_frequency_and_duration(df_helper_id,
                                 start_date_str,
                                 end_date_str,
                                 transition_date_str)
    
    if channel_name in easter_eggs.keys():
        st.write(easter_eggs[channel_name])
    else:
        st.write("""Hello ADA explorer. I hope that you are enjoying the moment. Let's try another channel!""")
