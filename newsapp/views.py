from django.shortcuts import render
import requests
import json
# Create your views here.


def index(request):
    country = request.GET.get("country")
    category = request.GET.get("category")
    if country:
        r = requests.get(f"http://newsapi.org/v2/top-headlines?country={country}&apiKey=088172d976e842f695598f5ee909a2a7")
        list_data= r.json()
        articles = list_data['articles']
    else:
        r = requests.get(f"http://newsapi.org/v2/top-headlines?category={category}&apiKey=088172d976e842f695598f5ee909a2a7")
        list_data= r.json()
        articles = list_data["articles"]
    return render(request, 'app/index.html', context={
            'articles':articles,
            
    })

  

## API 
# URL = https://newsapi.org/v2/top-headlines?country=us&apiKey=088172d976e842f695598f5ee909a2a7
