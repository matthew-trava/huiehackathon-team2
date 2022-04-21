# import streamlit as st
from inspect import CO_VARKEYWORDS
from wordcloud import STOPWORDS, WordCloud
import pandas as pd
from collections import Counter
import nltk
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

# nltk.download('wordnet')
# nltk.download('omw-1.4')

def get_text_data(df_path, column_list):
    return pd.read_csv(df_path, usecols=column_list)

cols_2020 = ['row hash', 'service delivery affect reasons', 'service delivery change description']
df_2020 = get_text_data('data/raw/2020 Survey Data.csv', cols_2020)

service_delivery_2020 = df_2020['service delivery affect reasons'].dropna().tolist()

# def lemma_remove_stop(lst):
#     lemmatizer = WordNetLemmatizer()
#     lemmatised_sentences = [[lemmatizer.lemmatize(word.lower()) for word in word_tokenize(sentence)] for sentence in lst]
#     tokens_wo_stop = [[word for word in sentence if not word in stopwords.words()] for sentence in lemmatised_sentences]
#     tokens = [[word for word in sentence if word.isalpha()] for sentence in tokens_wo_stop]
#     return tokens

from sklearn.feature_extraction.text import CountVectorizer
CountVec = CountVectorizer()
cv = CountVec.fit_transform(service_delivery_2020)
features = CountVec.get_feature_names()
features_count = cv.toarray().sum(axis = 0)
d = dict(zip(features, features_count))

# cols_2020 = ['row hash', 'service delivery affect reasons', 'service delivery change description']
# df_2020 = get_text_data('data/raw/2020 Survey Data.csv', cols_2020)

# service_delivery_2020 = df_2020['service delivery affect reasons'].dropna().tolist()
# stop = stopwords.words('english')
# for sentence in range(len(service_delivery_2020)):
#     tokens = word_tokenize(service_delivery_2020[sentence].lower())
#     tokens_wo_stop = [t for t in tokens if t not in stop]
#     service_delivery_2020[sentence] = " ".join(tokens_wo_stop)

# from sklearn.feature_extraction.text import CountVectorizer
# CountVec = CountVectorizer()
# cv = CountVec.fit_transform(service_delivery_2020)
# features = CountVec.get_feature_names()
# features_count = cv.toarray().sum(axis = 0)
# d = dict(zip(features, features_count))

# wordcloud = WordCloud(background_color = 'white', width = 600, height = 300).generate_from_frequencies(d)
# st.image(wordcloud.to_array())