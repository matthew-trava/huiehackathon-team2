import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd

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
        return "Postiive"
    
def get_subjectivity(string):
    doc = nlp(string)
    return doc._.blob.subjectivity

def subjectivity_groups(value):
    if value >= 0.5:
        return "More Subjective"
    else:
        return "More Objective"

def sentiment_matching(df, lst, year):
    tmp = pd.DataFrame()
    for item in lst:
        text = []
        sentiment = []
        subjectivity = []
        tempdf = df[df[item].notna()]
        tempdf['sentiment_score'] = tempdf[item].apply(get_sentiment)
        tempdf['sentiment_group'] = tempdf['sentiment_score'].apply(sentiment_groups)
        tempdf['subjectivity_score'] = tempdf[item].apply(get_subjectivity)
        tempdf['subjectivity_group'] = tempdf['subjectivity_score'].apply(subjectivity_groups)
        tempdf['category_assessed'] = item
        tmp = pd.concat([tmp, tempdf])
    tmp.to_csv(f'data/processed/sentiment/sentiment_linked/{year}.csv')
        

sentiment_matching(df20, ['priorities and concerns','important learning','comments'], 2020)
sentiment_matching(df21, ["Can you please tell us your organisations current key priorities and or concerns",
                                      'Can you tell us a short story about your experiences',
                                      'Is there anything else you would like to share with us or comment on'], 2021)
