# Page and Footer configurations
import streamlit as st
st.set_page_config(
     page_title="Team Tūī",
     page_icon="🐦",
     layout="wide",
     initial_sidebar_state="expanded",
)
hide_streamlit_style = """
	<style>
	/* This is to hide Streamlit footer */
	footer {visibility: hidden;}
	</style>
"""
st.markdown("""<style>
	/* This is to hide Streamlit footer */
	footer {visibility: hidden;}
	</style>""", unsafe_allow_html=True)

# Package Installations
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
@st.cache()
def nltk_downloads():
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
nltk_downloads()
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import sys
from nlp.word_cloud import word_cloud_generator

@st.cache
def df2020():
    return pd.read_csv('data/processed/df_2020_ohe.csv')
@st.cache
def df2021():
    return pd.read_csv('data/processed/df_2021_ohe.csv')

def spacer(height):
    for _ in range(height):
            st.write('\n')

# Completed
def home():
    """The main home page exploring details and including a mass link of directories"""

    st.write(
        """### Welcome to Team Tūī's Hackathon submission!
As part of our submission we've produced a series of analysis broken down into **6 key areas**.
Going through each of the **6 pages** you'll observe our findings and insights written alongside the graphs and imagery produced.
             """)
    
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    
    with col1:
        st.write("#### 2020 Summary")
        st.write("A dashboard style interface highlighting key information of the 2020 survey.")
    with col2:
        st.write("#### 2021 Summary")
        st.write("A dashboard style interface highlighting key information of the 2021 survey.")
    with col3:
        st.write("#### Year-to-Year Comparisons")
        st.write("We present questions that can be matched across both time periods")
    with col4:
        st.write("#### Clustering Analysis")
        st.write("In this portion we analyse similarity between respondents based off what they responded using clustering algorithms")
    with col5:
        st.write("#### Geographic Analysis")
        st.write("We assess question responses in relation to there location and/or location of impact")
    with col6:
        st.write("#### Natural Language Processing")
        st.write("Utilising a series of machine learning capabilities to understand entities within the text but also categorise similar comments/worded responses")

    st.write("___")
    with st.expander("Hackathon Backing Data"):
        col1, col2 = st.columns(2)
        with col1:
            st.write("""2020 Survey Data \n
[Dataset](https://www.huie.org.nz/survey-2020/download-the-time-to-shine-survey-dataset/) \n 
[Infographic](https://www.huie.org.nz/wp-content/uploads/COVID-19-Impact-Sector-Survey-Infographic.pdf) \n 
[Full Report](https://www.huie.org.nz/wp-content/uploads/Time-to-Shine-_COVID19-Impact-Community-Survey-Report.pdf)""")
    with col2:
            st.write("""2021 Survey Data \n
[Dataset](https://www.huie.org.nz/wp-content/uploads/COVID-Hauora-Wellbeing-Survey-dataset-291021.csv)\n
[Slides](https://www.huie.org.nz/wp-content/uploads/COVID-19-Hauora-Wellbeing-Research-slides.pdf)\n
[Full Report](https://www.huie.org.nz/wp-content/uploads/COVID-19-Hauora-Wellbeing-Report-2021.pdf)""")
    
    with st.expander("Our Team Name"):
        st.write("""
        ____
        ### Our Team Name
    
        Our team name comes from a bird found in New Zealand; a Tūī.
        It is a bird that is commonly found throughout both mainland and offshore islands.
        \n \n
        Further links to explore to learn more about the bird:\n
        - https://nzbirdsonline.org.nz/species/tui\n
        - https://www.youtube.com/watch?v=d0Fde3bCvZ0\n
        - https://www.nzbirds.com/birds/tui.html
        """)
    with st.expander("The Good Data Institute"):
        col1, col2 = st.columns([4,1])
        with col1:
            st.write("""
            ### The Good Data Institute
        
            A global community of ambitious data professionals.
            Our mission is to be the bridge between the not-for-profit world and the world of data analytics practitioners wishing to do social good. Using D&A, we identify, share, and help implement the most effective means for growing NFP people, organisations, and their impact. Our ultimate goal is social good. We believe that data and analytics has tremendous potential to help not for profit organisations achieve greater impact.\n
           [Read More Here!](https://www.gooddatainstitute.com/)
            """)
        with col2:
            st.markdown("***")
            st.image('assets/gdi-logo.png')
            st.markdown("***")

def dashboard2020():
    st.write("Dashboard 2020")
    st.write("coming soon....")
     
def dashboard2021():
    st.write("Dashboard 2021")
    st.write("coming soon....")

def yearcomparisons():
    st.write("## Year Comparisons")
    st.write("""
             We explore the changes occuring over the years throughout the two surveys collected by presenting the information
             side by side.\n\n\n***""")
    st.markdown("#### Changes in Service Delivery Over the Years")
    col1, col2 = st.columns(2)
    def column_builder(lst):
        for item in lst:
            st.image(f"joyce/{item}")
            spacer(2)
    with col1:
        st.markdown('#### 2020 Survey')
        service_delivery_2020 = ['Changes in the level of service delivery by organisation income - 2020.png', 
                                 'Changes in the level of service delivery by service type - 2020.png',
                                 'Changes in the level of service delivery by the number of paid staff - 2020.png',
                                 'Changes in the level of service delivery by the number of volunteers - 2020.png']
        column_builder(service_delivery_2020)                       
    with col2:
        st.markdown('#### 2021 Survey')
        service_delivery_2021 = ['Changes in the level of service delivery by organisation income - 2021.png', 
                                 'Changes in the level of service delivery by service type - 2021.png',
                                 'Changes in the level of service delivery by the number of paid staff - 2021.png',
                                 'Changes in the level of service delivery by the number of volunteers - 2021.png']
        column_builder(service_delivery_2021)
    _, col2, _ = st.columns(3)
    col2.image('joyce/Changes in the level of service delivery over time.png')
    st.markdown("***")
    st.markdown("#### Funding Resources Over the Years")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('#### 2020 Survey')
        funding_2020 = ['Funding reserve level by organisation income - 2020.png',
                        'Funding reserve level by service type - 2020.png',
                        'Funding reserve level by the number of paid staff - 2020.png',
                        'Funding reserve level by the number of volunteers - 2020.png']
        column_builder(funding_2020)
    with col2:
        st.markdown('#### 2021 Survey')
        funding_2021 = ['Funding reserve level by organisation income - 2021.png',
                        'Funding reserve level by service type - 2021.png',
                        'Funding reserve level by the number of paid staff - 2021.png',
                        'Funding reserve level by the number of volunteers - 2021.png']
        column_builder(funding_2021)
    _, col2, _ = st.columns(3)
    col2.image('joyce/Funding reserve levels over time.png')
    st.markdown("***")
    
    # Further comparisons
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('#### 2020 Survey')
        other20 = ['Sector changes 2020.png', 'Services changes 2020.png',
                   'Staffing changes 2020.png', 'Support accessed 2020.png',
                   'Support needed 2020.png']
        column_builder(other20)
    with col2:
        st.markdown('#### 2021 Survey')
        other21 = ['Sector changes 2021.png', 'Services changes 2021.png',
                   'Staffing changes 2021.png', 'Support accessed 2021.png',
                   'Support needed 2021.png']
        column_builder(other21)
    
def clusteringanalysis():
    st.write("Clustering")
    st.write("coming soon....")
   
def geographic():
    st.write("Geographic")
    st.write("coming soon....")
    
def nlpanalysis():
    st.write("## Year Comparisons")
    st.markdown("***")
    
    # Word Clouds
    with st.expander("Make 2020 WordClouds"):
        st.write("Explore any of the free text fields in the 2020 Survey Data through a word cloud!")
        select20 = st.selectbox("Description fields - 2020 Data", [
            'service delivery affect reasons', 'service delivery change description', 'challenges: Other (please specify)',
            'opportunities: Other (please specify)', 'priorities and concerns', 'support accessed: Other (please specify)',
            'other new ways', 'comments'])
        word_cloud_generator(df2020(), [select20])
    with st.expander("Make 2021 WordClouds"):
        st.write("Explore any of the free text fields in the 2021 Survey Data through a word cloud!")
        select21 = st.selectbox("Description fields - 2021 Data", [
            'service delivery affect reasons', 'service delivery change description', 'challenges: Other (please specify)',
            'opportunities: Other (please specify)', 'priorities and concerns', 'support accessed: Other (please specify)',
            'other new ways', 'comments'])
        # word_cloud_generator(df2021(), [select21])
    
    test = "Potato"
    st.markdown(f"""# <span style="color:blue">{test}</span>""", unsafe_allow_html=True)
        
    

def recommendations():
    st.write("Recommendations")
    st.write("coming soon....")

def main():
    # base header
    st.title("HuiE Hackathon: Team Tūī")
    
    # sidebar as applicable (can add additional sidebar items)
    with st.sidebar:
        col1, col2, col3 = st.columns([0.3, 1.5,0.5])
        st.image("assets/huielogo-edited.png", width = 300)
        st.title("Navigator")
        st.write(
            """
            #### This sidebar will allow you to navigate information not only about HuiE but also about the data analysis conducted and some of the insights drawn from the survey data over the past 2 years.
            _____
            """)
        page = st.radio("Select the page you want to explore!", 
                        ['Home', '2020 Summary', '2021 Summary', 'Year-to-Year Comparisons','Clustering Analysis',
                         'Geographic Analysis','Natural Language Processing','Recommendations'])
        st.write("_____")
        st.sidebar.write("""
        Team Members: Matthew, Joyce, Cynthia, Nicolas, & Raul
        \n Advisors: Shreyank & Shakeel
    _____""")
    
    # page navigation
    if page == "Home":
        home()
    elif page == "2020 Summary":
        dashboard2020()
    elif page == "2021 Summary":
        dashboard2021()
    elif page == "Year-to-Year Comparisons":
        yearcomparisons()
    elif page == "Clustering Analysis":
        clusteringanalysis()
    elif page == "Geographic Analysis":
        geographic()
    elif page == "Natural Language Processing":
        nlpanalysis()
    else:
        recommendations()

if __name__ == '__main__':
    main()

