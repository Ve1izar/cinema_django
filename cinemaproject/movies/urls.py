from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'), 
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'), 
    path('history/', views.movie_history, name='movie_history'),
    path('<int:movie_id>/toggle-watched/', views.toggle_watched, name='toggle_watched'),
]