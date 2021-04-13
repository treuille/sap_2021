import streamlit as st
import pandas as pd

#import python pages
from modules.home_page import run_home
from modules.pandas_page import run_pandas
from modules.graphs_page import run_graphs

#Set app name and emoji displayed in browser tab
st.set_page_config(page_title="Data Scientists", page_icon="bar_chart")

#title of my app and breif description
st.title("Data Science on Data Scientists")
st.subheader("Let's take a look at some data on actual Data Scientists! Time to get meta :face_with_monocle:")

#set up the side bar for page options
page = st.sidebar.radio("Pick a Page:", ["Home", "Pandas Profile", "Basic Graphs"])

#load data
train_set = pd.read_csv("data/aug_train.csv")

if page == "Home":
    run_home(train_set)

elif page == "Pandas Profile":
    run_pandas(train_set)

else:
    run_graphs(train_set)
