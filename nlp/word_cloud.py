import streamlit as st
from wordcloud import STOPWORDS, WordCloud
import pandas as pd
from collections import Counter
import nltk
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

# nltk.download('wordnet')
# nltk.download('omw-1.4')
stop = stopwords.words('english')
stop.append('level')
lemmatizer = WordNetLemmatizer()
CountVec = CountVectorizer()

def word_cloud_generator(df, lst):
    for x in lst:
        temp_df = df.reset_index()[x].dropna().to_list()
        for sentence in range(len(temp_df)):
            tokens = word_tokenize(temp_df[sentence].lower())
            tokens = [lemmatizer.lemmatize(word) for word in tokens]
            tokens_wo_stop = [t for t in tokens if t not in stop]
            temp_df[sentence] = " ".join(tokens_wo_stop)
        cv = CountVec.fit_transform(temp_df)
        features = CountVec.get_feature_names_out()
        features_count = cv.toarray().sum(axis = 0)
        wordcloud = WordCloud(background_color = 'white', width = 600, height = 300).generate_from_frequencies(
            dict(zip(features, features_count)))
        
        st.image(wordcloud.to_array())

# word_cloud_generator(df_2020, ['service delivery affect reasons', 'service delivery change description'])