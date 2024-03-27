from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .views import *
import os
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import requests

# Create your views here.


class MovieSearchView(APIView):

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='include_adult',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_BOOLEAN,
                required=False,
                description='Include adult content (true or false)',
                default=False
            ),
            openapi.Parameter(
                name='language',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description='Language code (e.g., "en-US")',
                default='en-US'
            ),
            openapi.Parameter(
                name='primary_release_year',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description='Primary release year of the movie',
            ),
            openapi.Parameter(
                name='page',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='Page number',
                default=1
            ),
            openapi.Parameter(
                name='region',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description='Region code',
            ),
            openapi.Parameter(
                name='year',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description='Release year of the movie',
            ),
        ]
    )
    def get(self, request, movie_name):

        url = f"https://api.themoviedb.org/3/search/movie"

        params = {
            'query': movie_name,
            'include_adult': request.query_params.get('include_adult', 'true'),
            'language': request.query_params.get('language', 'en-US'),
            'page': request.query_params.get('page', 1),
            'primary_release_year': request.query_params.get('primary_release_year', ''),
            'year': request.query_params.get('year', ''),
            'region': request.query_params.get('region', ''),
        }

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.environ.get('ACCESSTOKENAUTH')}"
        }

        response = requests.get(url, params=params, headers=headers)
        # print(response.url)

        if response.status_code == 200:
            return Response(response.json())
        elif response.status_code == 401:
            return Response({"error": "Unauthorized request. Please check your bearer token."}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error": "Failed to retrieve movie data"}, status=response.status_code)


class TVShowSearchView(APIView):

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='first_air_date_year',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='Search only the first air date. Valid values are: 1000..9999',
            ),
            openapi.Parameter(
                name='include_adult',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_BOOLEAN,
                required=False,
                description='Include adult content (true or false)',
                default=False
            ),
            openapi.Parameter(
                name='language',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description='Language code (e.g., "en-US")',
                default='en-US'
            ),
            openapi.Parameter(
                name='page',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='Page number',
                default=1
            ),
            openapi.Parameter(
                name='year',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description='Release year of the movie',
            ),
        ]
    )
    def get(self, request, tv_show_name):

        url = f"https://api.themoviedb.org/3/search/tv"

        params = {
            'query': tv_show_name,
            'first_air_date_year': request.query_params.get('first_air_date_year', ''),
            'include_adult': request.query_params.get('include_adult', 'true'),
            'language': request.query_params.get('language', 'en-US'),
            'page': request.query_params.get('page', 1),
            'year': request.query_params.get('year', ''),
        }

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.environ.get('ACCESSTOKENAUTH')}"
        }

        response = requests.get(url, params=params, headers=headers)
        # print(response.url)

        if response.status_code == 200:
            return Response(response.json())
        elif response.status_code == 401:
            return Response({"error": "Unauthorized request. Please check your bearer token."}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error": "Failed to retrieve TV show data"}, status=response.status_code)


class MovieDetailView(APIView):

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='language',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description='Language code (e.g., "en-US")',
                default='en-US'
            )
        ]
    )
    def get(self, request, movie_id):
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.environ.get('ACCESSTOKENAUTH')}"
        }

        params = {
            'language': request.query_params.get('language', 'en-US')
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return Response(response.json())
        elif response.status_code == 401:
            return Response({"error": "Unauthorized request. Please check your bearer token."}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error": "Failed to retrieve movie data"}, status=response.status_code)
