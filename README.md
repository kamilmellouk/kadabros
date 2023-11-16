<!-- ABOUT THE PROJECT -->
## About The Project

This project assignment was implemented by the Kadabros team (see below for group members) for the <a href="https://epfl-ada.github.io/teaching/fall2023/cs401/">CS401 Appplied Data Analysis</a> course at <a href="https://www.epfl.ch">EPFL</a>. It builds on the YouNiverse dataset studied and made available by [Manoel Horeira](https://zenodo.org/records/4650046).

<p align="right">(<a href="#top">back to top</a>)</p>

## Abstract

In this data analysis story, we will focus on exploring the dynamics of the "People & Blogs" category on YouTube from 2006 to 2019. This YouTube category encompasses content primarily focused on individuals or groups sharing personal experiences, opinions, and daily activities. It includes a wide range of video types, such as vlogs, lifestyle content, and commentary. The emergence of the "People & Blogs" category can be traced back to the early days of YouTube, gaining prominence as users increasingly sought to share their lives, interests, and perspectives in a more personal and informal manner. This category has since evolved into a diverse space, reflecting the individuality and creativity of content creators within the YouTube community. It remains a vibrant and relevant group, with people rebranding their channels into the genre more and more.

Our analysis delves into the evolution of subcategories within "People & Blogs," investigates how YouTube channels strategically navigate and benefit from subcategory trends, and explores the specific evolution of the Vlog subcategory. Our aim is to understand when and why channels eventually have transitioned into or out of the People & Blogs categories over the past decade, and mostly what consequences the shift had on their audience and popularity.

<p align="right">(<a href="#top">back to top</a>)</p>

## Research questions

The goal of this research is to get insights on the emergence of the People & Blogs YouTube category and its evolution since then. Its final purpose lies in understanding the effects that getting into this genre of uploads can subsequently have on a channel's growth. To do so, we will explore the data and look to answer these auxiliary questions:

* When did the "People & Blogs" category come to life and how did its popularity fare in comparison to other genres ?
* How do YouTube channels within the category leverage the popularity of their respective subcategories?
* How does a YouTube subcategory's popularity within "People & Blogs" evolve over time?
* What insights can be gained from the evolution of Vlog videos within "People & Blogs" over time (considering factors such as length, views, likes, dislikes, and comments)?
* How did Youtube channels morphing either into or out of the People & Blogs categories fare after the transition ? E.g. how was a channel's popularity affected after migrating from Gaming to Vlog ?

<p align="right">(<a href="#top">back to top</a>)</p>

## Methods

*How do YouTube channels within the "People & Blogs" category leverage the popularity of their respective subcategories?*

For this question, we will conduct an analysis of channel behaviors, exploring factors such as upload frequency, content diversity, tag usage etc..

*Evolution of Vlog videos within "People & Blogs":*

This analysis will involve exploring trends over time, considering video length, views, likes, dislikes, and comments to understand the changing landscape of Vlog content within the "People & Blogs" category.

*How did Youtube channels morphing either into or out of the People & Blogs categories fare after the transition ?:*

To address the impact of transitioning channels in and out of the "People & Blogs" category, our approach involves identifying these transitions using metadata. We will then analyze various popularity metrics (views, likes, dislikes, comments, and subscriber counts) before and after the transition. Additionally, we will examine user engagement patterns during this period and compare the performance of transitioning channels with those of similar profiles that remain static in the prior category. Qualitative analysis of content changes and statistical significance testing will be employed to provide a comprehensive understanding of how these category transitions influence a channel's popularity.

<p align="right">(<a href="#top">back to top</a>)</p>

## Proposed timeline

The team plans to follow the timeline below for the project:

1. **Exploratory Data Analysis (EDA)**: Conduct initial analysis to identify trends and patterns within the subcategory. The general basis of this will be done in the scope of the P2 Milestone.
2. **Channel Strategy Analysis**: Investigate how YouTube channels in the "People & Blogs" category strategically leverage subcategory popularity.
3. **Vlog Subcategory Evolution Analysis**: Dive deeper into the evolution of Vlog videos, considering factors like video length, views, likes, dislikes, and comments.
4. **Identifying Category Transitions**: Implement methods to identify instances where YouTube channels transitioned into or out of the "People & Blogs" category.
5. **Popularity Metrics Analysis for Transitioning Channels**: Collect and analyze popularity metrics (views, likes, dislikes, comments, and subscriber counts) for channels before and after category transitions.
6.  **Comparison with Static Category Channels**: Compare the performance of channels that underwent category transitions with channels that remained static in the "People & Blogs" category.
7.  **Qualitative Analysis of Content Changes**: Conduct qualitative analysis of content changes accompanying category transitions, reviewing video content, titles, and descriptions.
8.  **Statistical Significance Testing**: Apply statistical significance testing to validate observed changes in popularity metrics, ensuring results are not due to random variation.
9.  **Synthesis and Reporting**: Compile findings into a cohesive story, providing insights into the dynamics of the "People & Blogs" category on YouTube, with a particular focus on the impact of category transitions on channel popularity.

<p align="right">(<a href="#top">back to top</a>)</p>

## Project Structure
* `data_youniverse` folder: Given that our data is very large, we chose not to version control this folder. We will chose to name this folder `data_youniverse` and this will be the data path we will be working with.
* `utils folder`: Contains helper methods for our exploration.
* `notebooks`: Contains individual notebooks developed during the initial exploratory phase.
* `eda.ipynb`: Contains the main EDA of the data for our story.

<p align="right">(<a href="#top">back to top</a>)</p>

## Organization within the team

<p align="right">(<a href="#top">back to top</a>)</p>

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Python](https://www.python.org/)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [nltk](https://www.nltk.org/)
* [Jupyter Notebook](https://jupyter.org/)
