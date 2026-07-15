from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Movie
from .forms import MovieForm

from imdb import Cinemagoer

WATCHLIST_SESSION_ID = 'watchlist'

# Список всіх елементів
def movie_list(request):
    sort_by = request.GET.get('sort', '-rating')
    
    allowed_sorts = ['rating', '-rating', 'title', '-release_date']
    if sort_by not in allowed_sorts:
        sort_by = '-rating'
        
    movies = Movie.objects.all().order_by(sort_by)
    
    featured_movies = Movie.objects.all().order_by('-rating')[:3]
    
    return render(request, 'movies/movie_list.html', {
        'movies': movies, 
        'featured_movies': featured_movies,
        'current_sort': sort_by
    })

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
    
    messages.success(request, f'🔘 Статус фільму "{movie.title}" змінено!')
    return redirect('movie_detail', movie_id=movie.id)

# Адмін-панель
def custom_admin_panel(request):
    movies = Movie.objects.all()
    return render(request, 'movies/admin_panel.html', {'movies': movies})

# Видалення фільму
def delete_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        movie_title = movie.title
        movie.delete()
        messages.error(request, f'🗑 Фільм "{movie_title}" було назавжди видалено!')
        
    return redirect('custom_admin_panel')

# Додавання нового фільму
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # Просто зберігаємо форму в базу!
            messages.success(request, '🎬 Новий фільм успішно додано!')
            return redirect('custom_admin_panel')
    else:
        form = MovieForm()

    return render(request, 'movies/add_movie.html', {'form': form})

# Редагування фільму
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save() # Просто зберігаємо оновлену форму!
            messages.success(request, f'✏️ Зміни для фільму "{movie.title}" збережено!')
            return redirect("custom_admin_panel")
    else:
        form = MovieForm(instance=movie)

    return render(
        request, "movies/edit_movie.html", {"form": form, "movie": movie}
    )

# Перегляд списку запланованих фільмів
def watchlist_view(request):
    # Отримуємо список ID фільмів з сесії (якщо порожньо - повертаємо порожній список [])
    watchlist_ids = request.session.get(WATCHLIST_SESSION_ID, [])
    
    # Дістаємо з бази даних лише ті фільми, ID яких є у нашому списку
    movies = Movie.objects.filter(id__in=watchlist_ids)
    
    return render(request, 'movies/watchlist.html', {'movies': movies})

# Додавання фільму до списку
def add_to_watchlist(request, movie_id):
    watchlist = request.session.get(WATCHLIST_SESSION_ID, [])
    
    if movie_id not in watchlist:
        watchlist.append(movie_id)
        # Обов'язково перезаписуємо сесію, щоб Django зберіг зміни
        request.session[WATCHLIST_SESSION_ID] = watchlist
        messages.success(request, '🍿 Фільм додано до списку "Буду дивитися"!')
    else:
        messages.info(request, 'Цей фільм вже є у вашому списку.')
        
    # Повертаємо користувача на ту сторінку, з якої він натиснув кнопку
    return redirect(request.META.get('HTTP_REFERER', 'movie_list'))

# Видалення фільму зі списку
def remove_from_watchlist(request, movie_id):
    watchlist = request.session.get(WATCHLIST_SESSION_ID, [])
    
    if movie_id in watchlist:
        watchlist.remove(movie_id)
        request.session[WATCHLIST_SESSION_ID] = watchlist
        messages.error(request, '🗑 Фільм видалено зі списку запланованих.')
        
    return redirect(request.META.get('HTTP_REFERER', 'watchlist_view'))