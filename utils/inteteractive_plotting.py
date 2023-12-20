import plotly.graph_objs as go
import pandas as pd
import streamlit as st


def video_frequency_and_duration_int(channel_id,
                                     df_feather,
                                     channel_name,
                                     start_date=None,
                                     end_date=None,
                                     transition_date=None):

    df_feather['year_month'] = pd.to_datetime(df_feather['year_month']
                                              .dt.to_timestamp())
    if start_date:
        df_feather = df_feather[df_feather['year_month'] >=
                                pd.to_datetime(start_date)]
    if end_date:
        df_feather = df_feather[df_feather['year_month'] <=
                                pd.to_datetime(end_date)]

    mean_duration = df_feather.groupby('year_month')['duration'].mean() / 60
    video_count = df_feather.groupby('year_month').size()

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=mean_duration.index, y=mean_duration,
                             mode='lines+markers',
                             name='Mean Duration (min)',
                             line=dict(color='blue')))

    fig.add_trace(go.Bar(x=video_count.index, y=video_count,
                         name='Video Count',
                         marker_color='blue',
                         opacity=0.4))

    if transition_date:
        fig.add_vline(x=pd.to_datetime(transition_date),
                      line_dash="dash",
                      line_color="red")

    fig.update_layout(title='Mean Video Duration and Video Count per Month',
                      xaxis_title='Upload Month',
                      yaxis_title='Mean Video Duration [minutes]',
                      yaxis2=dict(title='Number of Videos',
                                  overlaying='y',
                                  side='right'),
                      legend=dict(orientation="h",
                                  yanchor="bottom",
                                  y=1.02,
                                  xanchor="right",
                                  x=1))

    st.plotly_chart(fig)
