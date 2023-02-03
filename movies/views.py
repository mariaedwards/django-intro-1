"""Django views
"""
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Movie


def movies(request):
    """Movies View
    """
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})


def detail(request, movie_id):
    """Movie detail View
    """
    data = Movie.objects.get(pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': data})


def add(request):
    """Add a Movie View
    """
    title = request.POST.get('title')
    release_year = request.POST.get('release_year')
    director = request.POST.get('director')
    genre = request.POST.get('genre')
    if title and release_year and director and genre:
        movie = Movie(title=title, release_year=release_year,
                      director=director, genre=genre)
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(request, 'movies/add_movie.html')


def delete(_request, movie_id):
    """Movie delete View
    """
    try:
        movie = Movie.objects.get(pk=movie_id)
    except:
        raise Http404("Movie doesn't exist")

    movie.delete()
    return HttpResponseRedirect('/movies')


def home(_request):
    """Home View
    """
    return HttpResponse('Home')
