from imdb import Cinemagoer
import os
import json
from datetime import datetime

class IMDBScraper():
    def __init__(self):
        self.movies_and_ids = {'Iron Man' : '0371746',
                            'Iron Man 2' : '1228705',
                            'Thor' : '0800369',
                            'Captain America: The First Avenger' : '0458339',
                            'Marvel\'s The Avengers' : '0848228',
                            'Iron Man 3' : '1300854',
                            'Thor: The Dark World' : '1981115',
                            'Captain America: The Winter Soldier' : '1843866',
                            'Guardians of the Galaxy' : '2015381',
                            'Avengers Age of Ultron' : '2395427',
                            'Ant-Man' : '0478970',
                            'Captain America: Civil War' : '3498820',
                            'Doctor Strange' : '1211837',
                            'Guardians of the Galaxy Vol. 2' : '3896198',
                            'Spider-Man: Homecoming' : '2250912',
                            'Thor: Ragnarok' : '3501632',
                            'Black Panther' : '1825683',
                            'Avengers: Infinity War' : '4154756',
                            'Ant-Man and the Wasp' : '5095030',
                            'Captain Marvel' : '4154664',
                            'Avengers: Endgame' : '4154796',
                            'Spider-Man: Far From Home' : '6320628',
                            'Black Widow' : '3480822',
                            'Shang Chi and the Legend of the Ten Rings' : '9376612',
                            'Eternals' : '9032400',
                            'Spider-Man: No Way Home' : '10872600'}
        self.movie_list = []

    def build(self):
        self.ia = Cinemagoer()
    
    def call(self):
        self.movie = self.ia.get_movie(self.current_id)

    def extract_rating(self):
        self.rating = self.movie['rating']
    
    def results_to_json(self):
        self.movie_list.append({'MovieName' : self.current_movie,
                            'MovieId_imdb' : self.current_id,
                            'MovieRating' : self.rating})
    
    def pull_all_requests(self):
        for movie, id in self.movies_and_ids.items():
            now = datetime.now()
            print('===========================================\n')
            print('Scraping Ratings for "{}" -- {}'.format(movie, now.strftime('%m/%d/%Y, %H:%M:%S')))
            self.current_movie = movie
            self.current_id = id
            self.call()
            self.extract_rating()
            self.results_to_json()
            end = datetime.now()
            print('Scraping for "{}" completed -- time elapsed : {}'.format(movie, end -  now))
            print('\n===========================================\n')
    
    def save_json(self):
        print('\nWriting Data into JSON.')
        with open(os.path.join('data','movie_ratings.json'), 'w') as f:
            json.dump(self.movie_list, f)
        print('JSON file created\n')

def main():
    now = datetime.now()
    print('Initializing Scraper -- {}'.format(now.strftime('%m/%d/%Y, %H:%M:%S')))
    scraper = IMDBScraper()
    scraper.build()
    scraper.pull_all_requests()
    scraper.save_json()
    end = datetime.now()
    print('Scaper end -- {}'.format(end.strftime('%m/%d/%Y, %H:%M:%S')))
    print('Time Elapsed -- {}'.format(end - now))


if __name__ == '__main__':
    main()