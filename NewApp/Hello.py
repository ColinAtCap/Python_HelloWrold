#streamlit app

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Dataframe showing Uber data",
    page_icon=":blush:",
)
'''
### This page shows a Dataframe displaying Uber data for NY
'''

st.sidebar.title("Choose from these options")
#st.sidebar.text_input("How much data", key="nrows")
#progress_bar = st.sidebar.progress(0)
#status_text = st.sidebar.empty()

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

#progress_bar = st.sidebar.progress(100) 
user_data = load_data(20000)

'''#### Raw Data'''
#st.subheader('Raw data')
#st.write(user_data)

if st.sidebar.checkbox('Show histogram?'):
    st.subheader('Number of pickups by hour')
    hist_values = np.histogram(
        user_data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)

hour_to_filter = st.sidebar.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = user_data[user_data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
