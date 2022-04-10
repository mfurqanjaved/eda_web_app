from functools import cache
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


# titlw of webapp
st.markdown('''
# **Exploratory Data Analysis web application**
This app is developed by Furqan j. called by **EDA app**
 ''')

# how to upload file from pc

with st.sidebar.header("Upload your Data set (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file",type=["csv"])
    df=sns.load_dataset("titanic")
    # st.sidebar.markdown(("Example CSV file)(df)"))


# Profiling report

if uploaded_file is not None:
    @st.cache

    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df,explorative = True)
    st.header("Input DF**")
    st.write(df)
    st.write("---")
    st.header("**Profiling report with pandas")
    st_profile_report(pr)
else:
    st.info("Awaiting for csv file")
    if st.button("Press to use example data"):
        # example dataset

        def load_data():
            a = sns.load_dataset("iris")
            # columns = ["age","banana","codanics","duchland","ear"])
            return a
        df =load_data()
        pr =ProfileReport(df,explorative= True)
        st.header("**Input Dataframe**")
        st.write(df)
        st.write("---")
        st.header("**Pandas Profiling Report**")
        st_profile_report(pr)

