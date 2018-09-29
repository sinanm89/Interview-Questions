# Complete the function below.
# {
  # "page": "1",
  # "per_page": 10,
  # "total": 13,
  # "total_pages": 2,
  # "data": [
  #   {
  #     "Poster": "https://images-na.ssl-images-amazon.com/images/M/MV5BYjFhN2RjZTctMzA2Ni00NzE2LWJmYjMtNDAyYTllOTkyMmY3XkEyXkFqcGdeQXVyNTA0OTU0OTQ@._V1_SX300.jpg",
  #     "Title": "Italian Spiderman",
  #     "Type": "movie",
  #     "Year": 2007,
  #     "imdbID": "tt2705436"
  #   },
  # }
def fetch_movies(title, page=0):
    url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title={title}'.format(title=title)
    if page:
        url += '&page={page}'.format(page=page)
    req = urlopen(url)
    data = req.read()
    encoding = req.info().get_content_charset('utf-8')
    data = json.loads(data.decode(encoding))
    return data
        
def  getMovieTitles(substr):
#     get initial request
    data = fetch_movies(substr)
    out = [i.get('Title') for i in data.get('data')]
    total_pages = data.get('total_pages')
    page = data.get('page')
    page = 1
    while page < total_pages:
        page += 1
        data = fetch_movies(substr, page)
        for i in data.get('data'):
            out.append(i.get('Title'))
    out.sort()
    return out

