from PyMovieDb import IMDB
import pandas as pd

imdb = IMDB()
df = pd.read_csv('movies_box_office.csv')

flag = 0
with open('movies.json', 'a') as f:
    for movie in df['0']:
        print(movie)
        res = imdb.get_by_name(movie, tv = False)
        if '404' in res:
            continue
        if res is not None:
            f.write(res + '\n')