import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import streamlit as st

from utils.plotting import CATEGORY_COLORS


def get_date_range(start_date, end_date):
    return pd.period_range(start=start_date,
                           end=end_date,
                           freq='M')\
            .strftime("%Y-%m")


def visualize_evolution_of_channel(df_feather,
                                   channel_name,
                                   start_date=None,
                                   end_date=None,
                                   transition_date=None):
    df_feather = df_feather.copy()
    df_feather['year_month'] = pd.to_datetime(df_feather['year_month']
                                              .dt.to_timestamp())

    categories = df_feather['categories'].unique()

    # if start_date and end_date:
    #     assert start_date < end_date, "Start date must be before end date"

    if start_date:
        df_feather = df_feather[df_feather['year_month'] >=
                                pd.to_datetime(start_date)]
    if end_date:
        df_feather = df_feather[df_feather['year_month'] <=
                                pd.to_datetime(end_date)]

    fig = go.Figure()
    x_axis = get_date_range(df_feather['year_month'].min(),
                            df_feather['year_month'].max())

    for category in categories:
        # Default color if not defined
        category_color = CATEGORY_COLORS.get(category, 'gray')
        category_data = df_feather[df_feather['categories'] == category]
        category_count = category_data.groupby('year_month').size()

        category_count = category_count.reindex(x_axis,
                                                fill_value=0)
        fig.add_trace(go.Scatter(
            x=x_axis,
            y=category_count.values,
            mode='lines+markers',
            name=category,
            line=dict(color=category_color)
        ))

    if transition_date:
        fig.add_vline(x=pd.to_datetime(transition_date),
                      line_dash="dash",
                      line_color="red")

    fig.update_layout(title=f'Videos of channel {channel_name}',
                      yaxis_title='Number of Videos',
                      legend=dict(orientation="h",
                                  yanchor="bottom",
                                  y=1.02,
                                  xanchor="right",
                                  x=1))

    st.plotly_chart(fig)


def video_frequency_and_duration(df_feather,
                                 start_date=None,
                                 end_date=None,
                                 transition_date=None):
    df_feather = df_feather.copy()
    df_feather['year_month'] = df_feather['year_month'].dt.to_timestamp()

    if start_date:
        df_feather = df_feather[df_feather['year_month'] >=
                                pd.to_datetime(start_date)]
    if end_date:
        df_feather = df_feather[df_feather['year_month'] <=
                                pd.to_datetime(end_date)]
        
    mean_duration = df_feather.groupby('year_month')['duration'].mean() / 60
    video_count = df_feather.groupby('year_month').size()

    # Convert the index of mean_duration to PeriodIndex with monthly frequency
    mean_duration.index = pd.PeriodIndex(mean_duration.index, freq='M')
    video_count.index = pd.PeriodIndex(video_count.index, freq='M')

    x_axis = get_date_range(df_feather['year_month'].min(),
                            df_feather['year_month'].max())
    
    mean_duration = mean_duration.reindex(x_axis, fill_value=0)
    video_count = video_count.reindex(x_axis, fill_value=0)

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(x=x_axis,
                             y=mean_duration,
                             mode='lines+markers',
                             name='Mean Duration (min)',
                             line=dict(color='blue')),
                  secondary_y=False)

    fig.add_trace(go.Bar(x=x_axis,
                         y=video_count,
                         name='Video Count',
                         marker_color='blue',
                         opacity=0.4),
                  secondary_y=True)

    if transition_date:
        fig.add_vline(x=pd.to_datetime(transition_date),
                      line_dash="dash",
                      line_color="red")

    fig.update_layout(title='Mean Video Duration and Video Count per Month',
                      legend=dict(orientation="h",
                                  yanchor="bottom",
                                  y=1.02,
                                  xanchor="right",
                                  x=1))

    # fig.update_xaxes(title_text="Upload Month")

    fig.update_yaxes(title_text="Mean Duration (min)", secondary_y=False)
    fig.update_yaxes(title_text="Video Count", secondary_y=True)

    st.plotly_chart(fig)


def video_likes_and_views(df_feather, channel_name, start_date=None, end_date=None, transition_date=None):
    df_feather = df_feather.copy()
    df_feather['year_month'] = df_feather['year_month'].dt.to_timestamp()

    if start_date:
        start_date = pd.to_datetime(start_date).replace(day=1) 
        df_feather = df_feather[df_feather['year_month'] >= start_date]
    if end_date:
        end_date = pd.to_datetime(end_date).replace(day=1)  
        df_feather = df_feather[df_feather['year_month'] <= end_date]

    df_filtered = df_feather.groupby("year_month").agg({
        "like_count": "mean",
        "dislike_count": "mean",
        "view_count": "mean"
    })
    df_filtered["like_over_views_ratio"] = (df_filtered["like_count"] / df_filtered["view_count"])

    x_axis = get_date_range(df_feather['year_month'].min(), df_feather['year_month'].max())
    
    # Reindex the df_filtered to include all dates in x_axis, filling missing values with 0
    df_filtered = df_filtered.reindex(x_axis, fill_value=0)
    
    # Normalize mean views for marker sizes
    scaled_marker_size = ((df_filtered["view_count"] - df_filtered["view_count"].min()) /
                          (df_filtered["view_count"].max() - df_filtered["view_count"].min()) * 20) + 5

    fig = go.Figure(data=go.Scatter(
        x=x_axis,
        y=df_filtered["like_over_views_ratio"] * 100,  # Convert to percentage
        mode='markers',
        marker=dict(
            size=scaled_marker_size,
            color='blue',
            opacity=0.6
        ),
        name=channel_name
    ))

    if transition_date:
        transition_date = pd.to_datetime(transition_date).replace(day=1)  # Ensure transition_date is the first of the month
        fig.add_vline(x=transition_date, line_dash="dash", line_color="red")

    fig.update_layout(title="Like/Views Percentage with Views Indicated by Marker Size",
                      yaxis_title='Like/Views Ratio [%]',
                      legend=dict(orientation="h",
                                  yanchor="bottom",
                                  y=1.02,
                                  xanchor="right",
                                  x=1))

    st.plotly_chart(fig)