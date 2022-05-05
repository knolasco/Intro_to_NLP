"""
Read the csv, clean the data by extracting year from dates,
removing punctuations from article text, 
"""
import pandas as pd
import string
import os
import re

DATA_PATH = 'CNN_Articels_clean'

# load data
articles = pd.read_csv(os.path.join(DATA_PATH, 'CNN_Articels_clean.csv'))

# extract year
articles['Year'] = pd.to_datetime(articles['Date published'], format = '%Y-%m-%d %H:%M:%S').dt.year

# clean article text
def clean_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'[0-9]+', 'number', text)
    text = text.lower().split()
    return text

articles['text_cleaned'] = articles['Article text'].apply(clean_text)
print(articles.iloc[0]['text_cleaned'])