from django.urls import path
from .views import *

urlpatterns = [

    path('movie-detail',
         MovieDetailView.as_view(), name='movie-detail'),
]