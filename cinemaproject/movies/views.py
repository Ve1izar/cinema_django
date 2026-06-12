from django.shortcuts import render, get_object_or_404
from .models import Movie

# Список всіх елементів
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

# Детальна інформація
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id) 
    return render(request, 'movies/movie_detail.html', {'movie': movie})