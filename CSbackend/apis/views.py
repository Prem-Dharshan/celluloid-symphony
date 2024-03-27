from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .views import *
import tmdbsimple as tmdb
import os
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import *

# Create your views here.


class MovieSearchView(APIView):

    def get(self, request, movie_name):

        if movie_name:
            tmdb.API_KEY = os.environ.get("APIKEY")
            tmdb.REQUESTS_TIMEOUT = 5

            search = tmdb.Search()
            response = search.movie(query=movie_name)
            return Response(response)
        else:
            return Response({"error": "Movie name not provided"}, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailView(APIView):

    def get(self, request, movie_id):

        if movie_id:
            tmdb.API_KEY = os.environ.get("APIKEY")
            tmdb.REQUESTS_TIMEOUT = 5
            movie = tmdb.Movies(movie_id)
            response = movie.info()
            return Response(response)
        else:
            return Response({"error": "Movie name not provided"}, status=status.HTTP_400_BAD_REQUEST)

    