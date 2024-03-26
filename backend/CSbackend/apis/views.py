from django.shortcuts import render
import requests
from django.http import JsonResponse
import os
from dotenv import load_dotenv
from rest_framework.views import APIView
from requests import get

# Create your views here.

load_dotenv()

class MovieDetailView(APIView):

    def get(self, request):
        
        query =  request.GET.get('q')

        if (query):
            pass

        

