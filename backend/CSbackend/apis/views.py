from django.shortcuts import render
import requests
from django.http import JsonResponse
import os
from dotenv import load_dotenv

# Create your views here.

load_dotenv()

class MovieDetailView():

    def post(request):

        api_key = os.environ.get('APIKEY')
        

    
