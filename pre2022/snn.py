import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json


def get_titles(substr, page):
    # header =  {}
    url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title={substr}&page={page}'.format(
        substr=substr, page=str(page)
    )
    req = Request(url, method='GET')
    try:
        res = urlopen(req, timeout=5)
    except URLError:
        print('Something went wrong with the request.')
        raise
    except Exception as e:
        print('Something else went wrong with the request.')
        raise
    read_res = res.read()
    data = json.loads(read_res.decode("utf-8"))
    return data


def getMovieTitles(substr):
    data = get_titles(substr, 0)

    current_page = int(data.get("page")) #: The current page.
    total_movie_titles = data.get("total", 0) #: The total number of movies in the search result.
    total_pages = data.get("total_pages") #: The total number of pages which must be queried to get all the results.
    movie_data_list = data.get('data')

    titles = []
    i = 1

    while i < total_pages:
        for movie in movie_data_list:
            titles.append(movie.get('Title'))
        if len(titles) <= total_movie_titles:
            current_page += 1
            data = get_titles(substr, current_page)
            movie_data_list = data.get('data')
        else:
            break
        i += 1

    titles.sort()
    return titles

print(getMovieTitles('spiderman'))
