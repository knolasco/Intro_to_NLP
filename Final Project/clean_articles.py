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
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'[0-9]+', 'number', text)
    text = text.lower().split()
    return text

class DataManager:
    
    def __init__(self):
        self.DATA_PATH = 'CNN_Articels_clean_2'

    def load_data(self):
        self.data = pd.read_csv(os.path.join(self.DATA_PATH, 'CNN_Articels_clean.csv'))

    def extract_year(self):
        self.data['Year'] = pd.to_datetime(self.data['Date published'], format = '%Y-%m-%d %H:%M:%S').dt.year
    
    def clean_article_text(self):
        self.data['article_text_screen'] = self.data['Article text'].apply(clean_text)