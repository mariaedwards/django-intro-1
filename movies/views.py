"""Django views
"""
from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {'id': 1, 'title': 'The Shawshank Redemption', 'release_year': 1994,
            'director': 'Frank Darabont', 'genre': 'Drama'},
        {'id': 2, 'title': 'The Godfather', 'release_year': 1972,
            'director': 'Francis Ford Coppola', 'genre': 'Crime, Drama'},
        {'id': 3, 'title': 'The Dark Knight', 'release_year': 2008,
            'director': 'Christopher Nolan', 'genre': 'Action, Crime, Drama'},
        {'id': 4, 'title': 'The Godfather: Part II', 'release_year': 1974,
            'director': 'Francis Ford Coppola', 'genre': 'Crime, Drama'},
        {'id': 5, 'title': 'The Lord of the Rings: The Return of the King',
            'release_year': 2003, 'director': 'Peter Jackson', 'genre': 'Action, Adventure, Drama'}
    ]
}


def movies(request):
    """Movies View
    """
    return render(request, 'movies/movies.html', data)


def home(_request):
    """Home View
    """
    return HttpResponse('Home')
