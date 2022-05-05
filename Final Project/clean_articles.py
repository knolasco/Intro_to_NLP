"""
Read the csv, clean the data by extracting year from dates,
removing punctuations from article text, 
"""
import pandas as pd
import string
import os
import re

DATA_PATH = 'CNN_Articels_clean'

def clean_text(text):
    if type(text) == str:
        text = text.replace('CNN', '')
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = re.sub(r'[0-9]+', 'number', text)
        text = text.lower().split()
    else:
        text = ''
    return text

class DataManager:
    
    def __init__(self):
        self.DATA_PATH = 'CNN_Articels_clean_2'

    def load_data(self):
        self.data = pd.read_csv(os.path.join(self.DATA_PATH, 'CNN_Articels_clean.csv'))

    def extract_year(self):
        self.data['Year'] = pd.to_datetime(self.data['Date published'], format = '%Y-%m-%d %H:%M:%S').dt.year
    
    def clean_article_text(self):
        self.data['article_text_clean'] = self.data['Article text'].apply(clean_text)

    def filter_cols(self):
        self.data = self.data[['Headline', 'Category', 'Article text', 'Year', 'article_text_clean']]