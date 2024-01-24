import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport

# Function to preprocess data and create profile report
def create_profile_report(file_path):
    df = pd.read_excel(file_path)
    profile = ProfileReport(df)
    return profile
