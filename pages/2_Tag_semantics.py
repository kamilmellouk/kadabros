import streamlit as st
import pandas as pd
from streamlit import components


from urllib.error import URLError
st.header("Tag Semantics Analysis")

st.write(
    """
    Now, let us turn to the question on how YouTube channels within the category of People & Blogs leverage the popularity of their respective subcategories. But first, how can a subcategory defined? Follow us, as we unveil this by exploring the tags and how they are used in this context!
    """
)

st.subheader('Tags Evolution in People & Blogs')
st.write(
    """
    Let us begin by looking at the evolution of tags within the People & Blogs category.    
    """
)
with open('./plots/most_used_tags.html', 'r') as f:
    html_string = f.read()
components.v1.html(html_string, width=700, height=400, scrolling=False)
st.write(
    """
    The number of tags within People & Blogs shows a general upward trend over the years, with a peak in 2016 followed by a slight decrease in 2018. This pattern reveals an evolving recognition among YouTubers of the significance of tags in enhancing their videos' discoverability and visibility, thereby potentially elevating their status within their respective subcategories. The trend underscores a growing awareness that adept tagging can be a critical factor in the quest for popularity on the platform.
    
    Now, let us look at the distribution of tags used for YouTube videos within People & Blogs.     
    """
)

with open('./plots/distribution_of_tags.html', 'r') as f:
    html_string = f.read()
components.v1.html(html_string, width=700, height=400, scrolling=False)

st.write(
    """The distribution of tags is skewed to the right, showing that a larger number of videos have fewer tags, with the frequency diminishing as the number of tags increases. Most videos have a tag count in the lower range, with very few reaching towards the higher end of the spectrum; one video even has a tag count of over 100! According to YouTube's policy for tags 
    
"*Don't add too many tags in a single video or playlist. The more tags you add, the less relevant they become for viewers or listeners who are searching*",

which the YouTubers within People & Blogs seem to be adhering to this policy as the majority of videos contain less than 15 tags. 

Now let's look at how the average number of tags per video each year
    """
)

with open('./plots/avg_number_of_tags.html', 'r') as f:
    html_string = f.read()
components.v1.html(html_string, width=700, height=400, scrolling=False)

st.write(
    """In 2006, the average number of tags per video was 10. But over the next few years, 
    the trend began to shift. By 2013, that number had increased greatly to a peak of roughly 
    17 tags per video. And even beyond 2010, the graph shows that people consistently added more 
    or less 15 tags in their video.
    """
)

with open('./plots/most_used_tags.html', 'r') as f:
    html_string = f.read()
components.v1.html(html_string, width=700, height=400, scrolling=False)


st.write(
    """"
    Vlog is the most popular tag, with the highest count, 
    indicating that it is the most frequently occurring or 
    perhaps the most tagged within the "Blogs & People" category. 
    However, "vlog" is also accompanied by its' other word 
    classes such as "vlogger", "vlogging" etc. 
    The counts generally decrease for other subcategories like "funny", "family", "love", 
    and so on, showing a declining order of prevalence. This suggests that while vlogging is 
    the dominant type of content, there is still a significant diversity of topics that creators 
    focus on within this category.
    """
)
with open('./plots/lda.html', 'r') as f:
    html_string = f.read()
components.v1.html(html_string, width=700, height=400, scrolling=True)


