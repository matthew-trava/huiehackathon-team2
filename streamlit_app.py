# Streamlit Import and Configuration
import streamlit as st
import streamlit.components.v1 as components
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
from PIL import Image
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
from joyce.nicsvis import comparison_plots
from scipy import stats

# Loading the relevant databases with caching
@st.cache
def df2020():
    return pd.read_csv('data/processed/df_2020_ohe.csv')
@st.cache
def df2021():
    return pd.read_csv('data/processed/df_2021_ohe.csv')
@st.cache
def sentiment2020():
    return pd.read_csv('data/processed/sentiment/sentiment_linked/2020.csv', index_col='Unnamed: 0')
@st.cache
def sentiment2021():
    return pd.read_csv('data/processed/sentiment/sentiment_linked/2021.csv', index_col='Unnamed: 0')
@st.cache
def emotions2020():
    return pd.read_csv('data/processed/emotions/2020_emotions.csv', usecols = ['Field', 'text', 'emotions', 'score'])
@st.cache
def emotions2021():
    return pd.read_csv('data/processed/emotions/2021_emotions.csv', usecols = ['Field', 'text', 'emotions', 'score'])

# Making the relevant dataframe for exporting upon dynamic creation in emotion exporting
@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')

# function to create gaps between graphs
def spacer(height):
    for _ in range(height):
            st.write('\n')

# the cards template for sentiment scoring
def sentiment_cards(data,title,colour):
    """Making Sentiment Score Cards using Bootstrap"""
    st.markdown(f"""
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=yes">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>

<div class="card text-center border-{colour} mb-3" style="max-width: 15rem; height: 10rem">
  <div class="card-header bg-{colour} text">{title}</div>
    <div class="card-body">
        <h1 class="card-text">{data.shape[0]}</h1>
  </div>
</div>""", unsafe_allow_html=True)

# Completed
def home():
    """The main home page exploring details and including a mass link of directories"""

    st.write(
        """### Welcome to Team Tūī's Hackathon submission!
Our team has produced an analytics web application to analyse the recovery of the NFP sector in Aotearoa New Zealand. This application is open source and available in the public domain. You can access the source code in [Team Tui’s Github repo](https://github.com/matthew-trava/huiehackathon-team2). \n 
As part of our submission we've produced a series of analysis broken down into **5 key areas**.
Going through each of the **6 pages** you'll observe our findings and insights written alongside the graphs and imagery produced.\n
In the recommendations page we highlight some key findings and some areas to improving/updating the collection process, and potential other avenues of development.
             """)
    
    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns(2)
    
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
        st.write("#### Geographic Analysis")
        st.write("We assess question responses in relation to there location and/or location of impact")
    with col5:
        st.write("#### Natural Language Processing")
        st.write("Utilising a series of machine learning capabilities to understand entities within the text but also categorise similar comments/worded responses")

    st.write("___")
    
    # Identifying the information that backs the hackathon
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
    
    # Explaining where our team name comes from and it's origins and links to NZ
    with st.expander("Our Team Name"):
        left, right = st.columns([3,1])
        left.write("""
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
        right.image("https://i.pinimg.com/564x/27/84/79/278479a3a96b07e562fcba3f5d126a86.jpg")
        
    # High level explanation of GDI
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
            spacer(4)
            st.image('assets/gdi-logo.png')
            spacer(1)

# making the 2020 dashboards
def dashboard2020():
    """Our First Exploratory Data Analysis page for 2020 survey data"""
    st.markdown("""## Dashboard 2020\n
On this page we will explore some basic statistics and interpretations found within the 2020 dataset.
\n ***
                """)
    with st.expander("The Original Dataset and Reports"):
        st.markdown("""Below is the page where the original survey information is found with infographics and reports if you wish to delve into it further!""")
        components.iframe("https://www.huie.org.nz/our-work/survey-2020/", height = 400, scrolling = True)
    
    with st.expander("Cross Table"):
        st.markdown("""For options that are a yes or no style response they have been represented by a 1 and 0. A value of 1 indicates that it has been selected, whereas 0 indicates it has not been selected.""")
        column20_1 = st.selectbox("Select the First Column", list(df2020().columns))
        column20_2 = st.selectbox("Select the Second Column", list(df2020().columns))
        crosstab20 = pd.crosstab(df2020()[column20_1], df2020()[column20_2])
        st.dataframe(crosstab20)
        chi2, p, dof, expected = stats.chi2_contingency(crosstab20)
        st.markdown(f"Chi2 value= {chi2} \n\n p-value= {p} \n\n Degrees of freedom= {dof}")
   
    st.markdown("*** \n Dashboard")
    st.markdown("""<iframe width="900" height="600" src="https://datastudio.google.com/embed/reporting/49146c74-f1bb-4a5a-b586-c58dbcff11c4/page/fmPrC" frameborder="0" style="border:0" allowfullscreen></iframe>""",
                    unsafe_allow_html=True)
      
def dashboard2021():
    st.markdown("""## Dashboard 2021\n
On this page we will explore some basic statistics and interpretations found within the 2021 dataset.
\n ***
                """)
    with st.expander("The Original Dataset and Reports"):
        st.markdown("""Below is the page where the original survey information is found with infographics and reports if you wish to delve into it further!""")
        components.iframe("https://www.huie.org.nz/our-work/survey-2021/", height = 400, scrolling = True)
    with st.expander("Cross Table"):
        column21_1 = st.selectbox("Select the First Column", list(df2021().columns))
        column21_2 = st.selectbox("Select the Second Column", list(df2021().columns))
        crosstab21 = pd.crosstab(df2021()[column21_1], df2021()[column21_2])
        st.dataframe(crosstab21)
        chi22, p2, dof2, expected2 = stats.chi2_contingency(crosstab21)
        st.markdown(f"Chi2 value= {chi22} \n\n p-value= {p2} \n\n Degrees of freedom= {dof2}")
    st.markdown("*** \n Dashboard")
    st.markdown("""<iframe width="900" height="600" src="https://datastudio.google.com/embed/reporting/7939942b-f2b8-4c3c-9944-fb69a2309cd2/page/fmPrC" frameborder="0" style="border:0" allowfullscreen></iframe>""", unsafe_allow_html=True)
        

def yearcomparisons():
    st.write("## Year Comparisons")
    st.write("""
             We explore the changes occuring over the years throughout the two surveys collected by presenting the information
             side by side.\n\n\n***""")
    st.markdown("#### Changes in Service Delivery Over the Years")
    st.plotly_chart(comparison_plots("bar_service"), use_container_width=True)
    spacer(2)
    st.plotly_chart(comparison_plots("staff_service"), use_container_width=True)
    spacer(2)
    st.plotly_chart(comparison_plots("volunteers_service"), use_container_width=True)
    spacer(2)
    st.plotly_chart(comparison_plots("income_service"), use_container_width=True)
    spacer(2)
    st.plotly_chart(comparison_plots("ethnic_service"), use_container_width=True)
    spacer(2)
    st.plotly_chart(comparison_plots("type_service"), use_container_width=True)
    st.markdown("***")
    st.markdown("#### Funding Reserves Over the Years")
    st.plotly_chart(comparison_plots("bar_funding"), use_container_width=True)
    spacer(2)
    st.plotly_chart(comparison_plots("staff_funding"), use_container_width=True)
    spacer(2)
    st.plotly_chart(comparison_plots("volunteers_funding"), use_container_width=True)
    spacer(2)
    st.plotly_chart(comparison_plots("income_funding"), use_container_width=True)
    spacer(2)
    st.plotly_chart(comparison_plots("ethnic_funding"), use_container_width=True)
    spacer(2)
    st.plotly_chart(comparison_plots("type_funding"), use_container_width=True)
    st.markdown("***")
    st.markdown('#### Further Comparisons')
    st.plotly_chart(comparison_plots("sector_changes"), use_container_width=True)
    spacer(2)
    st.plotly_chart(comparison_plots("service_changes"), use_container_width=True)
    spacer(2)
    st.plotly_chart(comparison_plots("staff_changes"), use_container_width=True)
    spacer(2)
    st.plotly_chart(comparison_plots("support_accessed"), use_container_width=True)
    spacer(2)
    st.plotly_chart(comparison_plots("support_needed"), use_container_width=True)

   
def geographic():
    st.markdown(" ## Geographic")
    st.write("Here we analyse parcipation and its local impact from a geographical point of view.")
    
    # define paths to images
    fp_gis_particip_2020 = 'assets/gis/gis_-_partcipation_2020.png'
    fp_gis_particip_2021 = 'assets/gis/gis_-_partcipation_2021.png'
    fp_gis_gdp_pc = 'assets/gis/gis_-_gdp_percapita.png'

    # write images with year option
    gis_option = st.radio("Year", 
                        ['2020', '2021'])

    cols = st.columns(2)
    #st.write("_____")
    if gis_option == '2020':
        cols[0].image(fp_gis_particip_2020)
    elif gis_option == '2021': 
        cols[0].image(fp_gis_particip_2021)
    
    cols[1].image(fp_gis_gdp_pc)

def nlpanalysis():
    st.write("## Natural Language Processing")
    st.write("""Natural language processing (NLP) is an ever growing field of data science as it tries to draw insights and understanding from textual data; the most complex and nuanced type of information we can collect.\n 
Text data is hard to analyse because it is filled with linguistic nuances to determine underlying meaning and intent of the message being conveyed.
People can often understand the underlying meanings and the emotions that back the information presented through text data such as books, reviews and comments.
\n \n A large feature set of the information collected by Hui E was in the form of text; responses written by charity and voluntary organisations conveying an overall feeling or sentiment in regards to their challenges and future outlook.\n
To help us understand and analyse this textual data given we utilised three methods to understand and bring to light that information in a more palatable and analytical manner.
Explore the three types of analysis, and the following methods of interpretation by explanding the items below!""")
    
    with st.expander("Method 1: Word Clouds"):
        st.write("""Word Clouds represent the frequency of which a word occurs within a set of text (in our case, all times a word appears within the list of responses for that particular question).\n
The larger a word is the more frequent it has appeared and the smaller it is the less frequent it has appeared within the text.\n
One of the issues with text data is that often the same word appears but in different ways. Examples are:\n
> swimming, 
> swam, 
> swim, 
> swims
\n
All these words have the same "root" word that backs them - the word swim. In order to make it easier to interpret and understand we apply a **lemmatiser** which essentially bnrings words back to their word root form (producing a lemma). This differs to a **Stemmer** as it **makes the words produced valid** and
doesn't just remove plurality or other known endings from words.\n
Our word clouds hence are a function of all the words responded from the question by all respondants brought back to it's root and then visualised in the form of a word cloud.
\n \n
### Interpreting Word Clouds\n
Interpreting the word clouds can be as simple as seeing larger words as items more focused on and mentioned by survey responders and smaller words less discussed. \n
From the cloud of words you can also see common themes amongst the words and draw conclusions from there.
""")
        
    with st.expander("Method 2: Sentiment Analysis"):
        st.write(""" Sentiment analysis refers to the NLP technique that tries to extract whether a given word, sentence or larger block of text can be considered negative, positive or neutral in sentiment.\n
In order to do this we used a **lexicon based approach**. This approach utilises a large dictionary of words with a given sentiment score. Sentiment scores, ranging between -1 for negative sentiment to +1 for positive sentiment, given an indication as to how negative or positive text is.

### Two Approach\n
A lexicon based approach is only as good as the dictionary of words it has with it's associated sentiment scores. In order to understand that often these given different results we utilise both the textblob sentiment analysis and the
NLTK VADER (Valence Aware Dictionary for sentiment Reasoning). Both of these rule based sentiment approaches are adaptable and simple to use and transfer well to multiple types of text based data.\n
One of the key drawbacks however is that it may not consider all similar words and their context (like an embeddings based model). \n 
We used both methods and present however it is filtering on the textblob analysis.\n

### Our Sentiment Range
We determine a score greater than 0.25 as text that is positive in sentiment, scores between 0.25 and -0.25 as neutral, and less than -0.25 as negative.
The more positive (negative) a value is infers that there were more words/n-grams with positive (negative) sentiment present.

### Subjectivity Analysis
A subset to the sentiment analysis we also look at subjectivity within the text present. Subjectivity refers to how emotive a text or opinionated a text may be whereas objective would be text which seems to be more rooted, or written with, factual information in mind.\n
A score closer to 0 means the text more objective in nature and a score closer to 1 means the text is more subjective in nature.
""")
        
    with st.expander("Method 3: Emotions Analysis"):
        st.write("""
Beyond sentiment we endeavoured to understand the emotions present within the text itself. In order to do this we utilised a pre-trained algorithm trained on commentary data from Reddit to conclude and understand example emotions from the text data.\n
Further details on the pre-trained model can be found at: https://huggingface.co/arpanghoshal/EmoRoBERTa/tree/main \n

### Benefits of Emotions Analysis
A key benefit to understanding emotion is that it conveys more meaning that simple sentiment. Looking at emotions like admiration, approval and optimism frame people's understandings of how they're feeling about the current and future environment more so than what sentiment can derive without contextual embeddings.
""")
    st.markdown("***")
    
    # 2020 Analysis
    st.markdown("## 2020 Survey")
    with st.expander("2020 WordClouds"):
        st.write("Explore any of the free text fields in the 2020 Survey Data through a word cloud!")
        select20 = st.selectbox("Description fields - 2020 Data", [
            'service delivery affect reasons', 'service delivery change description', 'challenges: Other (please specify)',
            'opportunities: Other (please specify)', 'priorities and concerns', 'support accessed: Other (please specify)',
            'other new ways', 'comments'])
        word_cloud_generator(df2020(), [select20])
        
        st.write("""We note some key thematics are shown explicitly within the word clouds generated. Examples of insights are as follows: \n
**Service Delivery affect Reasons** - Lockdowns as a result of COVID appear to be the key issue faced with lots of focus towards face to face support and service to the community no longer being able to occur as a result of the restrictions. Limiting items like group work and client contact seemed to be the key themes.\n
**Priorities and Concerns** - Key themes of funding issues and needs appeared to be the most common concern and priority. Additionally sourcing people in the form of btoh staff and volunteers in order to meet priority service requirements.\n""")
    
    
    with st.expander("2020 Sentiment Analysis"):
        st.markdown("""
                    On certain textual data we conducted sentiment analysis using the Pasttern Analysis calculation methodology.
                    Beyond sentiment (positive, negative, and neutral) we also calculated the relative subjectivity / objectivity of the text.\n\n
                    You can see below the numbers present for each of the categories found and are able to manipulate the filters to see the data with the assumed sentiment and polarity.""")
        st.markdown("***")
        text_fields20 = st.selectbox('Select your question to see the resulting sentiment', list(sentiment2020()['category_assessed'].unique()))
        temp_sentiment20_df = sentiment2020()[sentiment2020()['category_assessed']==text_fields20]
        col1, col2, col3 = st.columns([2,2,2])
        with col1:
            sentiment_cards(temp_sentiment20_df[temp_sentiment20_df['sentiment_group_textblob']=="Positive"],"Positive",'success')
        with col2:
            sentiment_cards(temp_sentiment20_df[temp_sentiment20_df['sentiment_group_textblob']=="Neutral"],"Neutral",'warning')
        with col3:
            sentiment_cards(temp_sentiment20_df[temp_sentiment20_df['sentiment_group_textblob']=="Negative"],"Negative",'danger')
        
        st.dataframe(temp_sentiment20_df[['row hash', 'category_assessed',text_fields20,'sentiment_score_textblob', 'sentiment_group_textblob','sentiment_score_vader', 'sentiment_group_vader','sentiment_differences', 'subjectivity_score', 'subjectivity_group']])
        
        st.markdown("***")
        if st.checkbox("Want to download the 2020 sentiment file for this column to analyse further?"):
            csv = convert_df(temp_sentiment20_df)
            st.download_button('Press to Download',
                               csv,
                               'sentiment.csv',
                               'text/csv',
                               key='download-csv')
        
    with st.expander("2020 Emotions Analysis"):
        st.markdown("***")
        emotion_fields20 = st.selectbox("2020 Survey Fields", emotions2020()['Field'].unique())
        emotions20_select = st.multiselect("2020 Emotions Selections", emotions2020()['emotions'].unique(), default = 'optimism')
        if len(emotions20_select) == 0:
            temp_emotions20_df = emotions2020()[(emotions2020()['Field'] == emotion_fields20)]
        else:
            temp_emotions20_df = emotions2020()[(emotions2020()['Field'] == emotion_fields20) & (emotions2020()['emotions'].isin(emotions20_select))]
        st.metric("Total Options under Select", temp_emotions20_df.shape[0])
        st.dataframe(temp_emotions20_df)
        if st.checkbox("Download the emotions table for 2020 for the column selected"):
            csv = convert_df(temp_emotions20_df)
            st.download_button('Press to Download',
                               csv,
                               'emotions.csv',
                               'text/csv',
                               key='download-csv')
        
    
    st.markdown('***')
    st.markdown("## 2021 Survey")
    with st.expander("Make 2021 WordClouds"):
        st.write("Explore any of the free text fields in the 2021 Survey Data through a word cloud!")
        select21 = st.selectbox("Description fields - 2021 Data", [
            'Concern Group: Other concerns (please specify)','Can you please tell us the main reasons for these changes in service delivery?',
            'Five Main Challenges: Other (please specify)', 'Five Opportunities or Personal Outcomes: Other (please specify)',
            'Can you please tell us your organisations current key priorities and or concerns', 'Non Financial Support your Organisation Needs: Other (please specify)',
            'Adjustments: Other (please specify)', 'Can you give us some examples of other innovations and changes you have made or adopted?',
            'What sorts of changes do you think are needed to strengthen the tangata whenua, community and voluntary sector in the future? Other (Please specify).',
            'Can you please give us an example of collaboration, sharing, partnerships and/or strategic decisions your organisation has made with other organisations, groups and/or government departments (since the beginning of the COVID-19 pandemic)?',
            'Can you tell us a short story about your experiences','Is there anything else you would like to share with us or comment on'])
        word_cloud_generator(df2021(), [select21])
        
        st.write("""We note some key thematics are shown explicitly within the word clouds generated. Example of insights are as follows: \n
**Concern Group: Other concerns (please specify)** - Volunteers and community appears to be the main concerns outside the selectable options. Further to that funding was reinformed inclusive of further lockdown woes and support from government and other for-profit entities. One key theme noted was time and workload required to deliver.\n""")
    
    with st.expander("2021 Sentiment Analysis"):
        st.markdown("""
                    On certain textual data we conducted sentiment analysis using the Pasttern Analysis calculation methodology.
                    Beyond sentiment (positive, negative, and neutral) we also calculated the relative subjectivity / objectivity of the text.\n\n
                    You can see below the numbers present for each of the categories found and are able to manipulate the filters to see the data with the assumed sentiment and polarity.""")
        st.markdown("***")
        text_fields21 = st.selectbox('Select your question to see the resulting sentiment', list(sentiment2021()['category_assessed'].unique()))
        temp_sentiment21_df = sentiment2021()[sentiment2021()['category_assessed']==text_fields21]
        col1, col2, col3 = st.columns([2,2,2])
        with col1:
            sentiment_cards(temp_sentiment21_df[temp_sentiment21_df['sentiment_group_textblob']=="Positive"],"Positive",'success')
        with col2:
            sentiment_cards(temp_sentiment21_df[temp_sentiment21_df['sentiment_group_textblob']=="Neutral"],"Neutral",'warning')
        with col3:
            sentiment_cards(temp_sentiment21_df[temp_sentiment21_df['sentiment_group_textblob']=="Negative"],"Negative",'danger')
        
        st.dataframe(temp_sentiment21_df[['Respondent ID', 'category_assessed',text_fields21,'sentiment_score_textblob', 'sentiment_group_textblob','sentiment_score_vader', 'sentiment_group_vader','sentiment_differences', 'subjectivity_score', 'subjectivity_group']])
        
        st.markdown("***")
        if st.checkbox("Want to download the 2021 sentiment file for this column to analyse further?"):
            csv = convert_df(temp_sentiment21_df)
            st.download_button('Press to Download',
                               csv,
                               'sentiment.csv',
                               'text/csv',
                               key='download-csv')
        
    with st.expander("2021 Emotions Analysis"):
        st.markdown("***")
        emotion_fields21 = st.selectbox("2021 Survey Fields", emotions2021()['Field'].unique())
        emotions21_select = st.multiselect("2021 Emotions Selections", emotions2021()['emotions'].unique(), default = 'optimism')
        if len(emotions21_select) == 0:
            temp_emotions21_df = emotions2021()[(emotions2021()['Field'] == emotion_fields21)]
        else:
            temp_emotions21_df = emotions2021()[(emotions2021()['Field'] == emotion_fields21) & (emotions2021()['emotions'].isin(emotions21_select))]
        st.metric("Total Options under Select", temp_emotions21_df.shape[0])
        st.dataframe(temp_emotions21_df)
        if st.checkbox("Download the emotions table for 2021 for the column selected"):
            csv = convert_df(temp_emotions21_df)
            st.download_button('Press to Download',
                               csv,
                               'emotions.csv',
                               'text/csv',
                               key='download-csv')
        
def recommendations():
    st.markdown("## Recommendations & Stories")
    st.markdown("""Throughout this hackathon we've seen both interesting stories of perseverance and struggle come from the charities surveyed.\n
Alongside the stories there are a series of recommendations that we believe could improve the understanding and ecosystem that exists within Aotearoa/New Zealand\n
***""")
    st.markdown("#### Stories")
    st.markdown("""
Throughout exploring the data we saw stories of struggle and hardship from a series of volunteers with emotions of nervousness, sadness and disappointment as noted through our emotions analysis for the 202o survey. \n 
Some key quotes we identified were:
> I'm on heart medication for stress directly related to the effects of Covid and keeping the doors open to meet the needs of our families, stakeholders and staff \n 
> The stress levels have risen so high and I have been put on Oxygen Therapy to cope in the meantime. \n 
Alongside these stories from the 2020 Survey we saw signs/signals of recovery from the year-to-year comparison we did but also through the increased levels of optimism and positivity. \n 
Our year-to-year comparisons painted a picture of opportunity and service and funding recovery. \n
We not only see renewed confidence throughout the comparisons from the 2020 to the 2021 survey results but could also see this directly through the quotes and words from the survey responders such as:
> We as an organisation needed to fine tune our direct communication with tangata, in doing so, we realised that us reaching out to tangata fast tracked us to being real and follow through with words into realistic action. Worked hard at assisting people to be supported in their growing independence. We saw people becoming more resilient and self-reliant as a result. Quite a few people are no longer requiring our services as they saw an opportunity to change their lives and thrive by seizing new opportunities such as training and employment. The positive results with some people completely blew us out of the water. I think we have grown as a team and are working with people more dynamically, creatively, flexibly and delivering services to people's individual needs. \n

As a result of these stories we saw opportunities for improvement in services for supporting charity organisations through mental health services as we saw them struggle even during the recovery phases in 2021. \n
These types of services would allow volunteers and paid staff of charity organisations to better support their patrons and communities of which they serve.""")
    st.markdown("***")
    st.markdown("### Recommendations")
    with st.expander("Data Collection"):
        st.markdown("""
As we explored the data we noted some areas that the survey collection process could be streamlined and survey data made more coherent. This includes consistent questions over time, logic within the surveys, and different data export methods. \n 
*** \n
#### Consistent Questions Over Time
By comparing the 2020 to the 2021 survey we noticed that some of the data is inconsistent in terms of the questions asked. This was noticed more closely with the breadth of questions expanding in 2021 to including multi-choice challenges and ongoing concern selection and the geographic data. \n 
By making the questions the same, or easily comparable, throughout future surveys it will allow for more consistent analysis of changes, improvements, recovery or downfall into the future for these charities. \n
In particular, the geographic analysis would be more consistent if it was translated into a common set of parameters for the NZ geography in alignment with the NZ Geographic data provided from the Government to allow ease of comparability between density data from NZ such as population densities and GDP densities as well as other quality of life information like crime rates and services in an easy to develop manner with little to no manual data transformation. \n 

#### Logic within the Survey
Integrating branching and logic within the survey allows for unique understanding to occur. This will also prevent data overlaps from occuring due to clashing questions such as in the example shown below.
""")
        st.markdown("""<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSerf6-IDaHCzM3Q1FjYJl6z6ab0o_PjiCbHYpAXSCcPh2QLDA/viewform?embedded=true" width="640" height="563" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>""", unsafe_allow_html=True)
        st.markdown("""
#### Different Data Export Methods
By exporting the data from the survey collection tool into formats like *JSON* it will allow for hierarchal structuring and easier analysis of multi-choice data analysis. This allows for easier visualisation of choices made by each charity with fewer required data transformations to make it easily understandable. JSON can also be interpreted from dashboard builders, limiting barrier to use by other individuals.
""")
        st.json("""{
	"id": "ABCDEFG",
	"type": "Charitable Trust",
	"name": "Charity of NZ",
	"Staff": "1-5 Staff",
	"Regions":
		{
			"Regions":
				[
					{ "id": "1", "area": "Waikato" },
					{ "id": "2", "area": "Auckland" },
					{ "id": "3", "areas": "Wellington" }
				],
	"Other Countries":
				[
					{ "id": "C1", "country": "Australia" },
					{ "id": "C2", "country": "Indonesia" }
				]
		},
	"Main Concerns":
		[
			{ "id": "M1", "concern": "Volunteer Numbers", "priority": 1},
			{ "id": "M2", "concern": "Mental Health Services", "priority": 2},
			{ "id": "M3", "concern": "Funding", "priority": 3}
		]
  }""")
    with st.expander("Areas of Further Exploration"):
        st.markdown("With our analysis we saw some areas of further exploration and actions that could be taken to develop the strength of the region.")
        st.markdown("***")
        st.markdown("""
#### Funding Deep Dives
We've seen some recent work from the Hui E team on exploring funding avenues to explore further. One way to improve those recommendations made (Link found [here](https://www.huie.org.nz/community-funding-white-paper-2022/) would be by identifying key funding surveys in further deep dive surveys. \n 
By performing a deep dive survey it would allow nuanced understanding of sources and the dynamics at play amongst organisations to understand where the main drivers are for lower revenue/funded organisations to that of larger one's heigtening areas of improvement like knowing what types of organisations get their funding from rather than broader generalisations.""")
        st.markdown("An example of a funding network deep dive can be show here: https://onlinelibrary.wiley.com/doi/full/10.1002/nml.21426")
        st.markdown("""
#### Network Deep Dives
In the 2021 survey the majority of organisations noted that the networks they developed as a key driver of their future success. One deep dive that could be explored in smaller follow up surveys would be to ask charities of other networks they work with in their region as building up these networks allow for possible cross funding to occur as well as expansion into services performed across region allowing organisations to act as collective units when searching for funding or information.
This could be done by allowing them to select from a list of registed charities as per the [Charities NZ Website](https://www.charities.govt.nz/charities-in-new-zealand/the-charities-register/open-data/) where they identify all currently reigsted charities in an open manner. Further to this it then can be back-linked to the entity relation diagram produced by Charities NZ allowing for matching data across the different NZ-wide information gathered for further exploration and analysis in the long-run.
""")
        st.image("assets/network_analysis_example.jpeg")
        st.caption("Image Sourced from: https://www.evalacademy.com/articles/social-network-analysis-what-we-learned")
    with st.expander("Sharing Knowledge"):
        st.markdown("""
One large avenue to explore as an area to improve is the access of knowledge of services beyond Government that can support these charitable organisations. \n 
Through the creation of things like a community dashboard you could possibly provide them knowledge and access to other charities in their regions looking for support or cross-collaboration or services to allow them to grow and access a wider network of technology, services, and people""")
        st.markdown("An example is shown here below through just a two column system")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### Technology to Help")
            st.markdown(" - https://www.microsoft.com/en-us/microsoft-365/nonprofit")
        with col2:
            st.markdown("##### Organisations Helping the Helpers")
            st.markdown(" - https://www.gooddatainstitute.com/")
        spacer(2)
        st.markdown("By providing this knowledge it truly allows for them to feel a renewed sense of community as they recover out of the pandemic but also show that there's others out there looking for help but also willing to help.")

        

def main():
    # base header
    st.markdown("""# <span style="color:#353455">Hui E Hackathon: Team Tūī</span>""", unsafe_allow_html=True)
    
    # sidebar as applicable (can add additional sidebar items)
    with st.sidebar:
        col1, col2, col3 = st.columns([0.3, 1.5,0.5])
        st.image("assets/huielogo-edited.png", width = 300)
        st.title("Navigator")
        st.write(
            """
            #### This sidebar will allow you to navigate information not only about Hui E but also about the data analysis conducted and some of the insights drawn from the survey data over the past 2 years.
            _____
            """)
        page = st.radio("Select the page you want to explore!", 
                        ['Home', '2020 Summary', '2021 Summary', 'Year-to-Year Comparisons',
                         'Geographic Analysis','Natural Language Processing','Recommendations & Stories'])
        st.write("_____")
        st.sidebar.write("""
        Team Members: Matthew, Joyce, Nicolas, Raul, & Cynthia
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
    elif page == "Geographic Analysis":
        geographic()
    elif page == "Natural Language Processing":
        nlpanalysis()
    else:
        recommendations()

if __name__ == '__main__':
    main()

