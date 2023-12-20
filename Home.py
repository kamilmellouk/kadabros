import streamlit as st

st.set_page_config(
    page_title="Kadabros",
    page_icon="📹",
)

st.markdown("""
## Kadabros' Data Analysis Story on the Youniverse Dataset
In this data analysis story, we will focus on exploring the dynamics of the
            "People & Blogs" category on YouTube from 2006 to 2019. This
            YouTube category encompasses content primarily focused on
            individuals or groups sharing personal experiences, opinions,
            and daily activities. It includes a wide range of video types,
            such as vlogs, lifestyle content, and commentary. The emergence
            of the "People & Blogs" category can be traced back to the early
            days of YouTube, gaining prominence as users increasingly sought
            to share their lives, interests, and perspectives in a more
            personal and informal manner. This category has since evolved
            into a diverse space, reflecting the individuality and creativity
            of content creators within the YouTube community. It remains a
            vibrant and relevant group, with people rebranding their channels
            into the genre more and more.

Our analysis delves into the evolution of subcategories within
            "People & Blogs," investigates how YouTube channels
            strategically navigate and benefit from subcategory
            trends, and explores the specific evolution of the Vlog
            subcategory. Our aim is to understand when and why channels
            eventually have transitioned into or out of the People & Blogs
            categories over the past decade, and mostly what consequences
            the shift had on their audience and popularity.

## Research Questions
The goal of this research is to get insights on the emergence of the
            People & Blogs YouTube category and its evolution since then.
            Its final purpose lies in understanding the effects that getting
            into this genre of uploads can subsequently have on a channel's
            growth. To do so, we will explore the data and look
            to answer these auxiliary questions:

* When did the "People & Blogs" category come to life and how did its
            popularity fare in comparison to other genres ?
* How do YouTube channels within the category leverage the popularity
            of their respective subcategories?
* How does a YouTube subcategory's popularity within "People & Blogs"
            evolve over time?
* What insights can be gained from the evolution of Vlog videos within
            "People & Blogs" over time (considering factors such as length,
                views, likes, dislikes, and comments)?
* How did Youtube channels morphing either into or out of the People & Blogs
            categories fare after the transition ? E.g. how was a channel's
            popularity affected after migrating from Gaming to Vlog ?


## Data Sources
This data story relies on the Youniverse dataset, made available by
            [Manoel Horeira](https://zenodo.org/records/4650046).
            This comprehensive repository encompasses YouTube channel
            data spanning the last decade (2005-2019). It encapsulates key
            metrics such as views, likes, comments, subscriber counts, and
            video metadata. The dataset's breadth and depth make it an ideal
            choice for our analysis, enabling a nuanced exploration of channel
            transitions within the People & Blogs category.

""")
