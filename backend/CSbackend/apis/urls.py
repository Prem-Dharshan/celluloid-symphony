from django.urls import path

from .views import *

urlpatterns = [
    path('', MovieDetailView.as_view(), name="movie-detail"),
    
]

