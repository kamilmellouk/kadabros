import os
import streamlit as st
# import pandas as pd

from streamlit import components
# from urllib.error import URLError

import base64

MAIN_PATH = os.getcwd()
WEB_DATA = os.path.join(MAIN_PATH, 'website_data')
LDA_PATH = os.path.join(WEB_DATA, 'lda.html')

st.header('Tag Semantics')

st.write(
    """
    Now, let us turn to the question on how YouTube channels within the category of People & Blogs 
    leverage tags to gain popularity within their channel. Follow us, as we unveil this by exploring the tags and how they are used in this context!
    """
)

st.subheader('Are Tags Even Used Within the People & Blogs Category?')

st.write(
    """
    Let's take a look at how tags within the People & Blogs category have evolved over time. 
    Do tags even matter? Are they still a viable tool for content 
    creators to reach their audiences? 
    """)

with open(os.path.join(WEB_DATA, 'number_of_tags.html'), 'r', encoding='utf-8') as f:
    html_string = f.read()
st.components.v1.html(html_string, width=700, height=450, scrolling=False)



st.write(
    """
    Starting in 2006, the use of tags was relatively modest. 
    Content creators might have been just experimenting with 
    tags as a tool to attract viewers. However, by 2010, there's a noticeable uptick in tag usage, 
    hinting at a growing understanding of the platform's algorithms and how tags could drive visibility. \n
    
    Come 2012, we see an explosion in tag numbers, peaking around in 2018. 
    This era marks a golden age of content diversification, with creators 
    likely packing their videos with a variety of tags to reach the widest 
    audience possible. Perhaps the YouTube algorithm favored such a strategy during those 
    years, or maybe content creators were vying to stand out in an increasingly crowded space.
    
    The question now is whether this revelation also led to a higher number of tags per video. Did 
    content creators simply add more tags to their videos, or did they become more strategic in their tagging?
    Let's check it out and see how the average number of tags per video has evolved over time! 
    
    """
    
)

with open(os.path.join(WEB_DATA, 'avg_number_of_tags.html'), 'r', encoding='utf-8') as f:
    html_string = f.read()
st.components.v1.html(html_string, width=700, height=450, scrolling=False)

st.write(
    """
    Woah! Not what one would've expected! However, interestingly, the average number 
    of tags per video doesn't show the same dramatic peak! It seems to be growing steadily, indicating that while 
    the total number of tags used ballooned content creators within the People & Blogs category were becoming more strategic, 
    possibly honing in on the most effective tags rather than simply adding more. But what are these strategic tags?
    """
    
)
st.subheader('What Are The Most Used Tags?')

st.write(
    """
    While we now have discovered that tags are still used within the People & Blogs category,
    let's take a look at the most used tags within this category. This may also help convery 
    what the most popular topics are within this category.
    """
)

with open(os.path.join(WEB_DATA, 'most_used_tags.html'), 'r', encoding='utf-8') as f:
    html_string = f.read()
st.components.v1.html(html_string, width=700, height=450, scrolling=False)

st.write(
    """
 At first glance, it's evident that "vlog" is the most popular tag, 
 towering over others with its usage count nearing the 250,000 
 mark. This is followed by "funny" and "family" which suggests a significant
 number of content creators focus on family-oriented material, 
 and the tag "vlogger," indicating a personal branding approach.
 Notably, there is a lexical variation in the tags used: "vlog", 
"vlogger", "vlogging", "vlogger", and "vlogs" essentially refer to the same concept 
but differ in their grammar. 
This reflects an interesting aspect of tagging behavior where creators use different forms of 
a word to maximize visibility across search queries. \n

The tags "love" and "kids" are also quite prevalent, 
indicating a trend towards family and everyday life content. 
The presence of "review" and "daily" suggests a strong 
nclination towards regular content updates and product or 
experience reviews, which are important content strategies 
for engaging viewers. Further down the list, the tags "video," "fitness," "life," 
"health," and "makeup" appear, each with decreasing frequency 
but still significant in numbers. These tags represent niche 
areas within the broader People & Blogs category, from lifestyle
and wellness to beauty tutorials. \n
    """)

st.subheader('But... How Do The Most Subscribed Content Creators Within People & Blogs Use Their Tags ?')

st.write(
    """
    As we try to understand the most used tags within the People & Blogs category,
    we should also take a look at how the most subscribed content creators within this category use their tags.
    For this purpose, we will take a look at the top 10 most subscribed content creators within the People & Blogs category.
    These include a variety of content creators such as Jake Paul, Casey Neistat, BuzzfeedVideo, TedTalks and more. \n
    
    The Word Cloud works by sizing the tags based on their frequency:: 
    the more frequently a tag appears, the larger and bolder it is displayed. 
    """)


file_ = open(os.path.join(WEB_DATA, 'wordcloud_tags.gif'), "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url}" alt="wordcloud gif">',
    unsafe_allow_html=True
)

st.write(
    """
    The word cloud, representing popular tags from the most subscribed YouTubers in a 
    certain category, illustrates that these creators often employ self-referential tags. 
    These include their personal and channel names—examples being "Jake Paul" and "Roman 
    Atwood," as well as extensions of these with "Vlogs" appended. This strategy is 
    indicative of self-promotion and brand reinforcement, which is particularly effective 
    for those who have already established a significant presence within the YouTube 
    community. Beyond individual branding, generic terms like "vlogs" and "vlogging" are 
    also prevalent across various channels, denoting a common content format among these 
    creators. These frequent tags not only aid in discoverability but also signify the 
    content type that viewers can expect, serving as a universal signifier within the 
    digital content landscape.

    """)


#st.subheader('Identifying Subcategories Within People & Blogs')

#with open(LDA_PATH, 'r', encoding='utf-8') as f:
#    html_string = f.read()
    
#components.v1.html(html_string, width=1400, height=1000, scrolling=False)


