from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'), 
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'), 
    path('history/', views.movie_history, name='movie_history'),
    path('<int:movie_id>/toggle-watched/', views.toggle_watched, name='toggle_watched'),
    path('manage/', views.custom_admin_panel, name='custom_admin_panel'),
    path('<int:movie_id>/delete/', views.delete_movie, name='delete_movie'),
    path('manage/add/', views.add_movie, name='add_movie'),
    path('<int:movie_id>/edit/', views.edit_movie, name='edit_movie'),
    path('watchlist/', views.watchlist_view, name='watchlist_view'),
    path('watchlist/add/<int:movie_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/remove/<int:movie_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
]