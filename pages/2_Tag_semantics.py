import os
import streamlit as st
# import pandas as pd

from streamlit import components
# from urllib.error import URLError

import base64

MAIN_PATH = os.getcwd()
WEB_DATA = os.path.join(MAIN_PATH, 'website_data')
LDA_PATH = os.path.join(WEB_DATA, 'lda.html')

st.header('Tag Semantics in People & Blogs')

st.write(
    """
    Now, let us turn to the question on how YouTube channels within the category of People & Blogs 
    leverage the popularity of their respective subcategories. But first, how can a subcategory defined? 
    Follow us, as we unveil this by exploring the tags and how they are used in this context!
    """
)

st.subheader('Tag Behaviour in People & Blogs')
with open(os.path.join(WEB_DATA, 'avg_number_of_tags.html'), 'r', encoding='utf-8') as f:
    html_string = f.read()
st.components.v1.html(html_string, width=700, height=450, scrolling=False)

st.write(
    """
    
    """
    
)


st.subheader('The Most Used Tags in People & Blogs')
with open(os.path.join(WEB_DATA, 'most_used_tags.html'), 'r', encoding='utf-8') as f:
    html_string = f.read()
st.components.v1.html(html_string, width=700, height=450, scrolling=False)

st.subheader('Wordcloud of Tags For The Most Subscribed YouTube Channels in People & Blogs')

file_ = open(os.path.join(WEB_DATA, 'wordcloud_tags.gif'), "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url}" alt="wordcloud gif">',
    unsafe_allow_html=True
)

#with open(LDA_PATH, 'r', encoding='utf-8') as f:
#    html_string = f.read()
#components.v1.html(html_string, width=1400, height=1000, scrolling=True)

