from django.urls import path
from .views import *

urlpatterns = [

    path('movie-search/<str:movie_name>',
         MovieSearchView.as_view(), name='movie-search'),
    path('movie-detail/<int:movie_id>',
         MovieDetailView.as_view(), name='movie-detail'),
]