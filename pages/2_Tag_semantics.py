import streamlit as st
import pandas as pd
from streamlit import components


from urllib.error import URLError

st.write(
    """
    This demo shows how to use `st.write` to visualize Pandas DataFrames.
    """
)

with open('./lda.html', 'r') as f:
    html_string = f.read()
components.v1.html(html_string, width=1000, height=600, scrolling=True)

