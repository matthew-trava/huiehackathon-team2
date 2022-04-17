import pandas as pd
import numpy as np
import spacy

# Data Load 
df_test = pd.read_csv('data/raw/2020 Survey Data.csv')

nlp = spacy.load('en_core_web_sm')
def entity_extraction(x):
    if x.isnan:
        return np.NaN
    doc = nlp(x)
    tokens = [token.text for token in doc]
    entities = [(entity.text,entity.label_)for entity in doc.ents]
    inc = 0
    for ent in doc.ents:
        x = x.replace(str(ent), str(inc))
        inc += 1
    y = x.split()
    z = x
    for value in range(len(y)):
        try:
            if y[value].isnumeric() == True:
                y[value] = entities[int(y[value])]
        except:
            next  
    return y

def post_entity_formatting(x):
    test = entity_extraction(x)
    if test.isnan:
        return np.NaN
    for x in range(len(test)):
        if x > 0:
            if type(test[x]) != tuple:
                test[x] = f" {test[x]}"
    return test


df_test = df_test[['row hash','sector changes: Other (please specify)']]
df_test['new_column'] = df_test.apply(lambda x: post_entity_formatting(x['sector changes: Other (please specify)']), axis = 1)
print(df_test.head())
