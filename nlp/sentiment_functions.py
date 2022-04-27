import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sent_obj = SentimentIntensityAnalyzer()

nlp = spacy.load('en_core_web_md')
nlp.add_pipe('spacytextblob')

df20 = pd.read_csv('data/processed/df_2020_ohe.csv')
df21 = pd.read_csv('data/processed/df_2021_ohe.csv')

def get_sentiment(string):
    doc = nlp(string)
    return doc._.blob.polarity
def sentiment_groups(value):
    if value <= -0.4:
        return "Negative"
    elif value <= 0.4:
        return "Neutral"
    else:
        return "Positive"
    
def get_vader_sentiment(string):
    return sent_obj.polarity_scores(string)['compound']

def sentiment_groups(value):
    if value <= -0.25:
        return "Negative"
    elif value < 0.25:
        return "Neutral"
    else:
        return "Positive"
    
def get_subjectivity(string):
    doc = nlp(string)
    return doc._.blob.subjectivity

def subjectivity_groups(value):
    if value >= 0.5:
        return "More Subjective"
    else:
        return "More Objective"

# Citation for Vader Sentiment Analysis
# Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
# Sentiment Analysis of Social Media Text. Eighth International Conference on
# Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

def sentiment_matching(df, lst, year):
    tmp = pd.DataFrame()
    for item in lst:
        text = []
        sentiment = []
        subjectivity = []
        tempdf = df[df[item].notna()]
        # Using the Textblob Sentiment Analyser
        tempdf['sentiment_score_textblob'] = tempdf[item].apply(get_sentiment)
        tempdf['sentiment_group_textblob'] = tempdf['sentiment_score_textblob'].apply(sentiment_groups)
        
        # Using the Vader Sentiment Analyser
        tempdf['sentiment_score_vader'] = tempdf[item].apply(get_vader_sentiment)
        tempdf['sentiment_group_vader'] = tempdf['sentiment_score_vader'].apply(sentiment_groups)
        
        # Getting the subjectivity of the scores
        tempdf['subjectivity_score'] = tempdf[item].apply(get_subjectivity)
        tempdf['subjectivity_group'] = tempdf['subjectivity_score'].apply(subjectivity_groups)
        
        tempdf['sentiment_differences'] = tempdf.apply(lambda x: x['sentiment_group_textblob']==x['sentiment_group_vader'], axis=1)
        
        tempdf['category_assessed'] = item
        tmp = pd.concat([tmp, tempdf])
    tmp.to_csv(f'data/processed/sentiment/sentiment_linked/{year}.csv')
        

sentiment_matching(df20, ['priorities and concerns','important learning','comments'], 2020)
sentiment_matching(df21, ["Can you please tell us your organisations current key priorities and or concerns",
                                      'Can you tell us a short story about your experiences',
                                      'Is there anything else you would like to share with us or comment on'], 2021)



