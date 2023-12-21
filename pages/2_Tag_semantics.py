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
    But first, let's take a look at how tags within the People & Blogs category have evolved over time!
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
    tags as a tool to attract viewers. However, by the beginning of the 2010's, there's a noticeable uptick in tag usage, 
    hinting at a growing understanding of the platform's algorithms and how tags could drive visibility. \n
    
    Come 2012, we see an explosion in tag numbers, peaking around in 2018. 
    This era marks a golden age of content diversification, with creators 
    likely packing their videos with a variety of tags to reach the widest 
    audience possible. Perhaps the YouTube algorithm favored such a strategy during those 
    years, or maybe content creators were dying to stand out in an increasingly crowded space.
    
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
    the total number of tags used ballooned, content creators within the People & Blogs category were becoming more strategic, 
    possibly honing in on the most effective tags rather than simply adding more. But what are these strategic tags?
    """
    
)
st.subheader('But... What Are The Most Used Tags?')

st.write(
    """
    While we now have discovered that tags are still used within 
    the People & Blogs category, let's delve deeper and explore 
    the most frequently used tags. This analysis will not only 
    shed light on the strategies of content creators but also 
    reveal the most popular topics within this category.
    """
)

with open(os.path.join(WEB_DATA, 'most_used_tags.html'), 'r', encoding='utf-8') as f:
    html_string = f.read()
st.components.v1.html(html_string, width=700, height=450, scrolling=False)

st.write(
    """
 At first glance, it's evident that "vlog" is the most popular tag, 
 towering over others with its usage count nearing over the 250,000 
 mark. This is followed by tags like "funny" and "family" which suggests a significant
 number of content creators focus on family-oriented material.
 Notably, there is a lexical variation in the tags used, i.e. "vlog", 
"vlogger", "vlogging", "vlogger", and "vlogs", which essentially refer to the same concept 
but differ in their grammar. 
This reflects an interesting aspect of tagging behavior where creators use different forms of 
a word to maximize visibility across search queries. \n

The tags "love" and "kids" are also quite prevalent, 
indicating a trend towards family and everyday life content. 
The presence of "review" and "daily" suggests a strong 
inclination towards regular content updates and product or 
experience reviews, which are important content strategies 
for engaging viewers. Further down the list, the tags "video," "fitness," "life," 
"health," and "makeup" appear, each with decreasing frequency 
but still significant in numbers. These tags represent niche 
areas within the broader People & Blogs category, from lifestyle
and wellness to beauty tutorials. \n
These tags span across multiple niches, 
from lifestyle and wellness to beauty tutorials. 
Given this variety, it prompts an intriguing question: 
Can we group these tags into specific topics or subcategories to 
better understand the content dynamics within the People & Blogs category?

    """)


st.subheader('Can We Group These Tags Into Topics Or Subcategories?')

st.write(
"""
Enter: Latent Dirichlet Allocation (LDA), a sophisticated topic modeling technique within Natural Language Processing (NLP) that can be used 
to discover the main topics within a corpus of text data. In short, LDA is probabilistic model that interprets a collection of data (such as a set of tags in our context) 
and yields a distribution of categories across the elements being analyzed. Although it resembles a clustering algorithm in some ways, LDA fundamentally differs by assigning 
probabilities indicating the likelihood of a tag being associated with a specific topic, rather than just placing it in a cluster. 
If you're interested in the math behind LDA, have a look at this [link](https://www.analyticsvidhya.com/blog/2021/08/a-brief-introduction-to-linear-discriminant-analysis/)!\n

We opted to train our LDA model using a specified number of topics, choosing 10 for our analysis as this showed the best distinct clustering. 
This training was conducted on a carefully selected random sample comprising 150,000 tags, all drawn from the People & Blogs category. \n 
Below you can interact with our LDA model! 

"""
)

with open(LDA_PATH, 'r', encoding='utf-8') as f:
    html_string = f.read()
    
components.v1.html(html_string, width=1400, height=800, scrolling=False)

st.markdown(
"""
After analyzing the results from our LDA model, 
we have pinpointed the top 30 key terms from a large dataset of 150,000 tags used in the People & Blogs category. 
To deepen our understanding and provide clearer insights, we have also created a 'topic' lookup table for reference.
 
1. **Lifestyle**: tags like `fitness`, `health`, `diet` and alike indicate a subcategory of lifestyle content.
2. **Family**: tags like `family`, `kids`, `baby` and alike indicate a subcategory of family-oriented content.
3. **Astrology**: listing all the horoscope signs as relevant terms, this topic indicates a subcategory of astrology content.
4. **Beauty**: beauty related tags seem to dominate the topic, implying a subcategory of beauty content.
5. **Entertainment**: `comedy`, `gaming`, `movie` seem to represent a broad range of entertainment.
6. **Food**: `cooking`, `food`, `recipe` represent a topic of food-related content.
7. **Social Media**: predominantly social medias this topic represents a subcategory of social media content.
8. **ASMR/Mukbang**: `asmr`, `mukbang` and alike represent a subcategory of ASMR/Mukbang content.
9. **News**: news orientied tags that seems to focus around `police`, `crime` and alike. 
10. **Book**: books and an interesting tag called `booktube` represent a subcategory of book content.
"""
)

st.write(
    """
    The People & Blogs category on YouTube is notably diverse, yet distinct subcategories emerge when analyzing tags through the LDA model. 
    While increasing the predefined number of topics could reveal more subcategories, a consistent finding is that nearly every distinct topic 
    includes some variation of "vlog." This suggests that vlogging is a prevalent content format within the People & Blogs category, with each 
    subcategory representing a variation of vlogging, distinguished by its unique content focus.
    """     
)

st.subheader('So... How Do The Most Subscribed Content Creators Within People & Blogs Use Their Tags ?')

st.write(
    """
    Given the discovery that subcategories within the People & Blogs category on YouTube largely consist of vlogging variations with distinct 
    content focuses, we will now explore the tagging strategies employed by the platform's most popular influencers in this category. For this 
    purpose, we will take a look at the top 10 most subscribed content creators within the People & Blogs category. 
    These include a variety of content creators such as Jake Paul, Casey Neistat, Lady Gaga, TedTalks and more. \n
    The generated word clouds below illustrate the most frequently used tags by these content creators! 
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
    Oh... So it seems that the most subscribed content creators seem to use tags that are more self-referential
    as the tags for almost each content creator's word cloud are their own names.  These include their personal and 
    channel names—examples being "Jake Paul" and "Roman Atwood," as well as extensions of these with "Vlogs" appended.
    This strategy is indicative of self-promotion and brand reinforcement, which is particularly effective for those
    who have already established a significant presence within the YouTube community. Beyond individual branding,
    generic terms like "vlogs" and "vlogging" are also prevalent across various channels, denoting a common content
    format among these creators. \n
    """)

