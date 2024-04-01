from django.shortcuts import render
import requests
from django.http import JsonResponse
import os
import environ
from rest_framework.views import APIView
from requests import get
import tmdbsimple as tmdb

env = environ.Env()
environ.Env.read_env()

# Create your views here.


class MovieDetailView(APIView):

    def get(self, request):

        # tmdb.API_KEY = env('APIKEY')
        # tmdb.REQUESTS_TIMEOUT = 5

        # search = tmdb.Search()
        # response = search.movie(request.query)
     
        # return response
        pass

        

