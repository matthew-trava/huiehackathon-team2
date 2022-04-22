# Package Installations
from matplotlib.figure import Figure
import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# import spacy
# from annotated_text import annotated_text
from st_aggrid import AgGrid
# from nltk import word_tokenize
# from nltk.corpus import stopwords
from streamlit_pandas_profiling import st_profile_report
import pandas_profiling
import plost


# Page and Footer configurations
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
    
@st.cache
def df_2020():
    return pd.read_csv('data/processed/df_2020_processed.csv')

@st.cache
def df_2021():
    return pd.read_csv('data/raw/2021 Survey Data.csv')

data_2020 = df_2020()
data_2021 = df_2021()

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

def dashboard2020():
    st.write("Dashboard 2020")
    st.write("coming soon....")
    # df_2020_raw = pd.read_csv('data/processed/df_2020_processed.csv')
    # st.markdown('### Organisation Type Statistics')
    # orgtype_columns = []
    # region_columns = []
    # for column in df_2020_raw.columns:
    #     if column.startswith('orgtype') == True and 'other' not in column:
    #         orgtype_columns.append(column)
    #     if column.startswith('region') == True and 'other' not in column:
    #         region_columns.append(column)

    # orgtype_sums = []
    # region_sums = []
    # for column in orgtype_columns:
    #     orgtype_sums.append(df_2020_raw[column].sum())
    # for column in region_columns:
    #     region_sums.append(df_2020_raw[column].sum())

    # orgtype_columns = [typ.replace("orgtype: ","") for typ in orgtype_columns]
    # options = st.multiselect('options', orgtype_columns)
    # col1, col2 = st.columns([2,3])
    # with col1:
    #     st.metric('Charitable Trust', data_2020['orgtype: charitable'].sum())
    #     # fig, ax = plt.subplots()
    #     # ax.pie(x = [data_2020['orgtype: charitable'].sum(), data_2020['row hash'].count() - data_2020['orgtype: charitable'].sum()],
    #     #     labels=['Charitable Trust', 'Not Charitable Trust'], autopct='%.0f%%')
    #     # st.pyplot(fig, width=10,height=10)
        
    #     df = pd.DataFrame(list(zip(orgtype_columns, orgtype_sums)), columns=['Type', "Total"])
    #     sub_df = df.loc[df['Type'].isin(options)]
    #     fig, ax = plt.subplots()
    #     ax.barh(y = sub_df['Type'].to_list(), width = sub_df['Total'].to_list())
    #     st.pyplot(fig)
    
    
def dashboard2021():
    st.write("Dashboard 2021")
    st.write("coming soon....")

def yearcomparisons():
    st.write("Year Comparisons")
    st.write("coming soon....")

def clusteringanalysis():
    st.write("Clustering")
    st.write("coming soon....")
   
def geographic():
    st.write("Geographic")
    st.write("coming soon....")
    
def nlpanalysis():
    st.write("NLP")
    st.write("coming soon....")

def recommendations():
    st.write("Recommendations")
    st.write("coming soon....")

def main():
    # base header
    st.title("HuiE Hackathon: Team Tūī")
    
    # sidebar as applicable (can add additional sidebar items)
    with st.sidebar:
        col1, col2, col3 = st.columns([0.5, 1.5,0.5])
        with col2:
            st.image("assets/huielogo.jpeg", width = 150)
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
        *Team Members: Matthew, Joyce, Cynthia, Nicolas, & Raul*
        \n *Advisors: Shreyank & Shakeel*
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
        # pr = pandas_profiling.ProfileReport(data_2020, title = "2020 Report", minimal = True)
        # st_profile_report(pr)

if __name__ == '__main__':
    main()

