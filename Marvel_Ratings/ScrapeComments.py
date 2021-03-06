from API_Keys.api_keys import MyKeys
from googleapiclient.discovery import build
import json
import os
from datetime import datetime

class CommentScraper():
    def __init__(self):
        self.movies_with_id = {'Iron Man' : '8ugaeA-nMTc',
                            'Iron Man 2' : 'wKtcmiifycU',
                            'Thor' : 'JOddp-nlNvQ',
                            'Captain America: The First Avenger' : 'JerVrbLldXw',
                            'Marvel\'s The Avengers' : 'eOrNdBpGMv8',
                            'Iron Man 3' : 'YLorLVa95Xo',
                            'Thor: The Dark World' : 'npvJ9FTgZbM',
                            'Captain America: The Winter Soldier' : '7SlILk2WMTI',
                            'Guardians of the Galaxy' : 'd96cjJhvlMA',
                            'Avengers Age of Ultron' : 'tmeOjFno6Do',
                            'Ant-Man' : 'pWdKf3MneyI',
                            'Captain America: Civil War' : 'dKrVegVI0Us',
                            'Doctor Strange' : 'HSzx-zryEgM',
                            'Guardians of the Galaxy Vol. 2' : 'wUn05hdkhjM',
                            'Spider-Man: Homecoming' : '39udgGPyYMg',
                            'Thor: Ragnarok' : 'ue80QwXMRHg',
                            'Black Panther' : 'xjDjIWPwcPU',
                            'Avengers: Infinity War' : '6ZfuNTqbHE8',
                            'Ant-Man and the Wasp' : 'UUkn-enk2RU',
                            'Captain Marvel' : 'Z1BCujX3pw8',
                            'Avengers: Endgame' : 'TcMBFSGVi1c',
                            'Spider-Man: Far From Home' : 'VUFmhKpZKlE',
                            'Black Widow' : 'ybji16u608U',
                            'Shang Chi and the Legend of the Ten Rings' : '8YjFbMbfXaQ',
                            'Eternals' : 'x_me3xsvDgk',
                            'Spider-Man: No Way Home' : 'ZYzbalQ6Lg8'}

        self.api_key = MyKeys().api_key
        self.movie_list = []

    def build_(self):
        self.youtube = build('youtube', 'v3', developerKey = self.api_key)

    def make_request(self):
        if self.next_page_token:
            self.request = self.youtube.commentThreads().list(
                                    part = 'snippet',
                                    videoId = self.current_id,
                                    pageToken = self.response['nextPageToken']
                                    )
        else:
            self.request = self.youtube.commentThreads().list(
                                    part = 'snippet',
                                    videoId = self.current_id,
                                    )
        self.response = self.request.execute()
    
    def results_to_json(self):
        self.movie_list.append({'MovieName' : self.current_movie,
                                'MovieId' : self.current_id,
                                'CommentAuthor' : self.author,
                                'OriginalComment' : self.comment})
    
    def fetch_elements(self):
        for element in self.response['items']:
            snippet = element['snippet']['topLevelComment']['snippet']
            self.comment = snippet['textOriginal']
            try:
                self.author = snippet['authorChannelId']['value']
            except:
                self.author = 'No Author Found'
            self.results_to_json()

    def pull_all_results(self):
        self.fetch_elements()
        threshold = 200 # so we don't exceed the request limit
        ind = 0
        while (ind < threshold) & ('nextPageToken' in self.response.keys()):
            self.next_page_token = True
            self.make_request()
            self.fetch_elements()
            ind += 1

    def find_movie_comments(self):
        # go through all movies in self.movies_with_id
        for movie_name, movie_id in self.movies_with_id.items():
            now = datetime.now()
            print('===========================================\n')
            print('Scraping Commments for "{}" -- {}'.format(movie_name, now.strftime('%m/%d/%Y, %H:%M:%S')))
            self.next_page_token = False
            self.current_movie = movie_name
            self.current_id = movie_id
            self.make_request()
            self.pull_all_results()
            end = datetime.now()
            print('Scraping for "{}" completed -- time elapsed : {}'.format(movie_name, end -  now))
            print('\n===========================================\n')

    def save_json(self):
        print('\nWriting Data into JSON.')
        with open(os.path.join('data','movie_comments.json'), 'w') as f:
            json.dump(self.movie_list, f)
        print('JSON file created\n')

def main():
    now = datetime.now()
    print('Initializing Scraper -- {}'.format(now.strftime('%m/%d/%Y, %H:%M:%S')))
    scraper = CommentScraper()
    scraper.build_()
    scraper.find_movie_comments()
    scraper.save_json()
    end = datetime.now()
    print('Scaper end -- {}'.format(end.strftime('%m/%d/%Y, %H:%M:%S')))
    print('Time Elapsed -- {}'.format(end - now))

if __name__ == '__main__':
    main()