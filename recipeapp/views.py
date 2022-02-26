from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    name = request.GET.get("mealname")
    category = request.GET.get("category")
    if name:

        url = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={name}")
        list_meal = url.json()
    else:
        url = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}")
        list_meal = url.json()
    context = {
        "meals":list_meal["meals"],
        
    }
   

#



    return render(request, "recipeapp/base.html",context)