import os
import streamlit as st
import pandas as pd

from streamlit import components

from urllib.error import URLError

MAIN_PATH = os.getcwd()
WEB_DATA = os.path.join(MAIN_PATH, 'website_data')
PEOPLE_BLOGS_PATH = os.path.join(WEB_DATA, 'People_&_Blogs')

st.header('The People & Blogs Category on YouTube')

st.markdown('<div style="text-align: justify;">Join us on a journey through YouTube\'s dynamic landscape as we unravel the transformation of channels within the People & Blogs category over the past decade. From sudden pivots to strategic shifts, we delve into the reasons behind channels morphing in this vibrant space. What motivates a channel\'s transition? Was it audience demand, a quest for reinvention, or a strategic play? Our quest is to uncover the motivations and quality that drove these channel metamorphoses. Get ready to decipher the narrative behind YouTube\'s shape-shifting channels as we navigate through data, decode patterns, and reveal the untold stories behind this intriguing evolution. Before diving into these relationships, let\'s take a step back and understand the People & Blogs category. What is it? What does it encompass? What are its most popular channels? Any category-specific dynamics ?</div>', unsafe_allow_html=True)

st.subheader('Why "People & Blogs" ?')

st.markdown('<div style="text-align: justify;">The original dataset only consists of channels with at least 10 videos and 10000 subscribers, so we won\'t need to filter out any channels. These thresholds ensure that we only consider channels with a significant amount of content and a large enough audience to be relevant, and are the basis of our analysis. A good place to start is to look at the distribution of channels across categories, to get a feel of eah category\'s size within the Youtube ecosystem.</div>', unsafe_allow_html=True)

with open(os.path.join(WEB_DATA, 'category_distribution.html'), 'r', encoding='utf-8') as f:
    html_string = f.read()
st.components.v1.html(html_string, width=700, height=450, scrolling=False)

st.markdown('<div style="text-align: justify;">These first numbers outline already a few heavyweight categories of the Youtube scene over that tiemscale, such as the Music and the Entertainment industries. Our analysis centers on the People & Blogs category due to its prominent representation and unique content dynamics. This category not only boasts a substantial channel count but also offers a diverse range of human-centric content, including personal narratives, vlogs, and informational videos. Moreover, it serves as an engagement magnet, drawing audiences seeking relatable and engaging content while fostering high interaction through comments, shares, and discussions. Additionally, People & Blogs stands out as a transition hotspot, historically attracting channels diversifying their content, making it an intriguing focal point for exploring the dynamic evolution and transitions within the YouTube ecosystem.</div>', unsafe_allow_html=True)

st.subheader('Average Metrics: Taking a Closer Look')

st.markdown('<div style="text-align: justify;">Pursuing the will to understand the overall size of the category, we will follow up by examining the average numbers that define a channel within the category. Basic computations on the "People & Blogs" dataframe returns an average number of 323 videos and 156,000 subscribers for channels in this subdivision (keep in mind the initial requirements for the channels we are studying, having discarded entries with under 10,000 subscribers or less than 10 uploads). These numbers are interesting for multiple reasons. The average video count is the second lowest across all categories, only behind Comedy (287), outlining the relatively recent emergence of this sector in the ecosystem, when compared to the mainstays that are f.e. Sports & Gaming. The mean subscriber count, again, seems on the lower end for Youtube, however its rise and competitiveness in the scene is only testament to its growing proportion of the focus. These numbers, although a good intuitive starting point to our understanding of the category, do not mean a lot at face value by themselves. In order to contextualize these figures, the following plots were used:</div>', unsafe_allow_html=True)

with open(os.path.join(WEB_DATA, 'videos_boxplot.html'), 'r', encoding='utf-8') as f:
    html_string = f.read()
st.components.v1.html(html_string, width=700, height=450, scrolling=False)

with open(os.path.join(WEB_DATA, 'subscribers_boxplot.html'), 'r', encoding='utf-8') as f:
    html_string = f.read()
st.components.v1.html(html_string, width=700, height=450, scrolling=False)

st.markdown('<div style="text-align: justify;">These boxplots reveal a few interesting insights. First, the video count distribution is heavily skewed to the right, with a median of 123 videos and a mean of 323. This indicates that the majority of channels in the category have a relatively low number of videos, with a few outliers having a much higher count. This is likely due to the fact that the category is relatively new, and that the majority of channels are still in their early stages. The subscriber count distribution is also skewed to the right, with a median of 35,000 subscribers and a mean of 156,000. For now then, it seems like the category\'s viewership is heavily dominated by a few channels. This analysis however raises a subsequent question: is there a correlation between the number of videos and the number of subscribers? We try to unearth a potential relationship in the next step.</div>', unsafe_allow_html=True)

with open(os.path.join(WEB_DATA, 'correlation.html'), 'r', encoding='utf-8') as f:
    html_string = f.read()
st.components.v1.html(html_string, width=700, height=450, scrolling=False)

st.markdown('<div style="text-align: justify;">This plot, complimented by a correlation matrix coefficient of 0.067 between the two variables, quie clearly reveal that there is no significant correlation between the number of videos and the number of subscribers, based on the data available to us. The category looks to be mostly populated by channels with few videos, with such channels\' popularity, subscriber wise, being of all sizes, ranging from 10k to 20M. All explorations till now point to the category\'s youth, with a few channels having already amassed a large following, and the rest still in the process of building their audience. We will now try to understand the category\'s evolution over time, and the underlyings behind its users\' dynamics.</div>', unsafe_allow_html=True)

st.subheader('People & Blogs: A Transition Hotspot')

st.markdown('<div style="text-align: justify;">Let us now try to get an initial idea of the evolving activity within the category, in order to grasp its dynamics and uncover relative trends. We will start by looking at the number of channels joining the studied genre over time, which will outline a first intuition regarding its trendiness.</div>', unsafe_allow_html=True)

with open(os.path.join(WEB_DATA, 'PB_Channel_Joins.html'), 'r', encoding='utf-8') as f:
    html_string = f.read()
st.components.v1.html(html_string, width=700, height=450, scrolling=False)

st.markdown('<div style="text-align: justify;">This vizualisation of the category\'s join dates reveals a steady increase in channel creation over the past decade. This is further strengthened by our linear regression line fit to the data, in order to better visualize the trend, revealsing a positive slope, aligning with the general perception of the genre\'s growth over that time frame. Interesting to note are a notable spike in 2016, as well as quite a dip from 2017. This could be due to a variety of reasons, such as a the emergence of vlogging and the rise of new content creators, as well as the increasing popularity of YouTube as a platform in the mid 2010s for example, and the subsequent saturation of the market. A good way to look into these popular trends is to look at the most popular channels within the category, as well as the most used tags at these times. This will constitute the next step of our analysis.</div>', unsafe_allow_html=True)