import streamlit as st
import pandas as pd

from urllib.error import URLError

st.write(
    """
    This demo shows how to use `st.write` to visualize Pandas DataFrames.

(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)
"""
)

DATA_PATH = "/data_youniverse"
df_channels_en = pd.read_csv(f"{DATA_PATH}/df_channels_en.tsv.gz", compression="infer", sep="\t") 
df_timeseries_en = pd.read_csv(f"{DATA_PATH}/df_timeseries_en.tsv.gz", compression="infer", sep="\t")

# plot general information on the dataset
st.write(df_channels_en.head())
st.write(df_channels_en.describe())
