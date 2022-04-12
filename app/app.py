# Package Installations
import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def home():
    st.balloons()
    wordcloud = WordCloud(background_color = 'white').generate("List of many words many many many yes yes yes words no no possiubly yes")
    st.image(wordcloud.to_array())
    


def main():
    # Main Display & Sidebar
    st.title("Team 2 - HuiE Hackathon!")
    
    with st.sidebar:
        st.title("Navigator")
        st.write(
            """
            #### This sidebar will allow you to navigate information not only about HuiE but also about the data analysis conducted and some of the insights drawn from the survey data over the past 2 years.
            _____
            """)
        page = st.radio("Select the page you want to explore!", 
                        ['Home', '2020 Summary', '2021 Summary', 'Year-to-Year Comparisons','Clustering Analysis',
                         '','Recommendations'])
    home()

if __name__ == '__main__':
    main()

