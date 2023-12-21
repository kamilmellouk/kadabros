import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

CATEGORY_COLORS = {
    "Science & Technology": "silver",
    "People & Blogs": "lightcoral",
    "Entertainment": "olivedrab",
    "Music": "khaki",
    "News & Politics": "orange",
    "Nonprofits & Activism": "palegreen",
    "Gaming": "peru",
    "Film & Animation": "skyblue",
    "Education": "blue",
    "Howto & Style": "plum",
    "Pets & Animals": "orchid",
    "Autos & Vehicles": "crimson",
    "Comedy": "forestgreen",
    "Sports": "lavender",
    "Travel & Events": "teal"
}


def plot_topN_tag(tag_col, N):
    tags_exploded = tag_col.str.split(',').explode()

    tags_count = tags_exploded.value_counts()

    top_tags = tags_count.head(N)
    top_tags.plot(kind='bar')
    plt.title(f'Top {N} Tags')
    plt.xlabel('Tags')
    plt.ylabel('Count')
    plt.show()


def video_frequency_and_duration(channel_id,
                                 df_feather,
                                 channel_name,
                                 start_date=None,
                                 end_date=None,
                                 transition_date=None,
                                 streamlit_plot=True):
    """
    Plots the mean video duration per month for given channels, with an
    optional vertical line indicating a category transition
    Plot moreover a histogram of the number of videos published.

    Parameters:
    - channel_id (str): YouTube channel ID.
    - df_feather (DataFrame): DataFrame containing
                              video data (already prefiltred).
    - channel name (str)
    - start_date (str, optional): Start date for filtering videos.
    - end_date (str, optional): End date for filtering videos.
    - transition_date (str, optional): Date to draw a vertical line
                                       indicating the category transition
    """

    plt.figure(figsize=(12, 6))
    ax1 = plt.gca()  # Primary axis
    ax2 = ax1.twinx()  # Secondary axis

    # Establish the full date range for x-axis
    start_period = pd.to_datetime(start_date).to_period('M') if start_date \
        else df_feather['year_month'].min()
    end_period = pd.to_datetime(end_date).to_period('M') if end_date \
        else df_feather['year_month'].max()
    full_period_range = pd.period_range(start=start_period,
                                        end=end_period,
                                        freq='M')

    alpha_level = 0.4  # Transparency for the bar plots

    mean_duration = df_feather.groupby("year_month")["duration"].mean() / 60
    mean_duration = mean_duration.reindex(full_period_range, fill_value=0)
    sns.lineplot(ax=ax1,
                 x=mean_duration.index.astype(str),
                 y=mean_duration.values,
                 marker="o",
                 color="blue",
                 label=f"{channel_name}")

    video_count = df_feather.groupby("year_month").size()
    video_count = video_count.reindex(full_period_range, fill_value=0)
    ax2.bar(video_count.index.astype(str),
            video_count.values,
            alpha=alpha_level,
            color="blue")

    if transition_date:
        transition_period = pd.to_datetime(transition_date).to_period('M')
        ax1.axvline(x=str(transition_period),
                    color='r',
                    linestyle='--',
                    label='Transition')

    ax1.set_xlabel("Upload Month")
    ax1.set_ylabel("Mean Video Duration [minutes]", color='black')
    ax2.set_ylabel("Number of Videos", color='black')
    ax1.tick_params(axis='y', colors='black')
    x_ticks = range(len(full_period_range))
    ax2.tick_params(axis='y', colors='black')
    ax1.set_xticks(x_ticks)
    ax1.set_xticklabels([period.strftime('%Y-%m')
                         for period in full_period_range],
                        rotation=90)

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

    plt.title("Mean Video Duration and Video Count per Month")
    plt.tight_layout()
    if streamlit_plot:
        st.pyplot()
    else:
        plt.show()


def video_likes_and_views(channel_id,
                          df_feather,
                          channel_name,
                          start_date=None,
                          end_date=None,
                          transition_date=None,
                          streamlit_plot=True):
    """
    Plots the mean video likes and views per month for given channels,
    with an optional vertical line indicating the category transition.
    The y axis represents the number of likes per view ratio,
    i.e. have people liked a lot the videos after watching?
    Size of the marker corresponds to the total views,
    i.e. have people watched a lot this channel?

    Parameters:
    - channel_id (str): YouTube channel ID.
    - df_feather (DataFrame): DataFrame containing video
                            data (already prefiltred).
    - channel name (str)
    - start_date (str, optional): Start date for filtering videos.
    - end_date (str, optional): End date for filtering videos.
    - transition_date (str, optional): Date to draw a vertical line
                                        indicating the category transition
    """

    plt.figure(figsize=(10, 6))

    # Establish the full date range for x-axis
    start_period = pd.to_datetime(start_date).to_period('M') if start_date \
        else df_feather['year_month'].min()
    end_period = pd.to_datetime(end_date).to_period('M') if end_date \
        else df_feather['year_month'].max()
    full_period_range = pd.period_range(start=start_period,
                                        end=end_period,
                                        freq='M')

    df_filtered = df_feather.groupby("year_month").agg({
        "like_count": "mean",
        "dislike_count": "mean",
        "view_count": "mean"
    })

    df_filtered["like_over_views_ratio"] = (df_filtered["like_count"] /
                                            df_filtered["view_count"])
    df_filtered = df_filtered.reindex(full_period_range, fill_value=0)

    # Normalize mean views to scale marker sizes
    scaled_marker_size = ((df_filtered["view_count"]
                          - df_filtered["view_count"].min()) /
                          (df_filtered["view_count"].max() -
                           df_filtered["view_count"].min()) * 100)

    plt.scatter(df_filtered.index.astype(str),
                df_filtered["like_over_views_ratio"],
                s=scaled_marker_size,
                label=channel_name,
                alpha=0.6,
                color="blue")   # , color=colors[channel_id]

    if transition_date:
        plt.axvline(x=transition_date,
                    color='r',
                    linestyle='--',
                    label='Transition')

    plt.xticks(rotation=90)
    plt.ylabel("Like/Views Ratio")
    plt.xlabel("Upload Month")
    plt.title("Like/Views Ratio per Month with Views Indicated by Marker Size")
    plt.legend()
    plt.tight_layout()
    if streamlit_plot:
        st.pyplot()
    else:
        plt.show()


def visualize_evolution_of_channel(channel_id,
                                   df_feather,
                                   channel_name,
                                   start_date=None,
                                   end_date=None,
                                   transition_date=None,
                                   streamlit_plot=True):
    '''
    Plots the evolution of video counts across different
    categories for a given channel.

    Parameters:
    - channel_id (str): The YouTube channel ID.
    - df_feather (DataFrame): DataFrame containing video data.
    - channels (DataFrame): DataFrame containing channel information.
    - start_date (str, optional): Start date for filtering videos.
    - end_date (str, optional): End date for filtering videos.
    - transition_date (str, optional): Date to draw a vertical line
                                        indicating the category transition.
    '''

    # df_filtered = df_feather[df_feather["channel_id"] == channel_id]
    df_filtered = df_feather
    # now df_feather is already pre filtred by the channel id
    categories = df_filtered['categories'].unique()

    # Set the full date range for x-axis
    start_period = pd.to_datetime(start_date).to_period('M') if start_date \
        else df_filtered['year_month'].min()
    end_period = pd.to_datetime(end_date).to_period('M') if end_date \
        else df_filtered['year_month'].max()
    full_period_range = pd.period_range(start=start_period,
                                        end=end_period,
                                        freq='M')

    plt.figure(figsize=(10, 5))

    for category in categories:
        # Check if the category has a defined color
        if category in CATEGORY_COLORS:
            category_color = CATEGORY_COLORS[category]
        else:
            category_color = 'gray'  # Default color if not defined

        category_data = df_filtered[df_filtered['categories'] == category]
        category_count = category_data.groupby('year_month').size()
        category_count = category_count.reindex(full_period_range,
                                                fill_value=0)
        plt.plot(category_count.index.astype(str),
                 category_count.values,
                 marker='o',
                 label=category,
                 color=category_color)

    if transition_date:
        plt.axvline(x=transition_date,
                    color='r',
                    linestyle='--',
                    label='Transition')

    plt.xticks(rotation=90)
    plt.ylabel("Number of Videos")
    plt.xlabel("Year-Month")
    plt.title(f"Videos of channel {channel_name}")
    plt.legend()
    plt.tight_layout()
    if streamlit_plot:
        st.pyplot()
    else:
        plt.show()
