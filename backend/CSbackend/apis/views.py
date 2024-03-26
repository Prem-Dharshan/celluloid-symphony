from django.shortcuts import render
import requests
from django.http import JsonResponse

# Create your views here.

import os
from dotenv import load_dotenv

load_dotenv()

class MovieDetailView():

    def post(request):

        api_key = os.environ.get('APIKEY')
        

    
