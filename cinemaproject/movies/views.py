from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm

# Список всіх елементів
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

# Детальна інформація
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id) 
    return render(request, 'movies/movie_detail.html', {'movie': movie})

# Історія переглядів
def movie_history(request):
    watched_movies = Movie.objects.filter(is_watched=True)
    return render(request, 'movies/movie_history.html', {'movies': watched_movies})

# Перемикання статусу
def toggle_watched(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    movie.is_watched = not movie.is_watched
    movie.save()
    
    return redirect('movie_detail', movie_id=movie.id)

# Адмін-панель
def custom_admin_panel(request):
    movies = Movie.objects.all()
    return render(request, 'movies/admin_panel.html', {'movies': movies})

# Видалення фільму
def delete_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        
    return redirect('custom_admin_panel')

# Додавання нового фільму
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('custom_admin_panel')
    else:
        form = MovieForm()

    return render(request, 'movies/add_movie.html', {'form': form})

# Редагування фільму
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)

        if form.is_valid():
            form.save()
            return redirect('custom_admin_panel')
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movies/edit_movie.html', {'form': form})