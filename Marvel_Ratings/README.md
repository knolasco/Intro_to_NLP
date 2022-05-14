# Description of Files

![marvel_cloud](marvel_cloud.png)

- [marvel_ratings.ipynb](https://github.com/knolasco/Intro_to_NLP/blob/master/Marvel_Ratings/marvel_ratings.ipynb)

This jupyter notebook contains the analysis for taking the YouTube comments and using them to predict the movie ratings.

- ScrapeComments.py

This python script uses the YouTube API to scrape comments from 26 Marvel Movies. The scraper collected a little under 100,000 comments.

- ScrapeIMDB.py

This python script uses the IMDB API to scrape movie ratings from the IMDB website. The ratings are used as the target variable in the jupyter notebook.

- /data

This folder contains the JSON files that are outputted from the scrapers. The JSON files are read into the notebook using Pandas.

- requirements.txt

Use this if you would like to run the notebook yourself! A simple "pip install -r requirements.txt" should do the trick.