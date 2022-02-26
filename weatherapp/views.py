from django.shortcuts import render
import json
import urllib.request



# Create your views here.
def index(request):
    if request.method=="POST":
        city = request.POST["city"]
        source = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=5f673a487aa1f75844d770a7f5c52780").read()
        list_of_data = json.loads(source)
        celsius=int(list_of_data['main']['temp']-273)
        data={
            'country': str(list_of_data["sys"]["country"]),
            'temp':str(celsius) + " C",
            'description':str(list_of_data["weather"][0]["description"]),
            'humidity':str(list_of_data['main']['humidity']) +  " %",
            'icon':list_of_data["weather"][0]['icon'],
            "city":city
        }
        print(data)
    else:
        data={}
    
    return render(request,'weather/base.html',data)
#api = api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
#api key = 5f673a487aa1f75844d770a7f5c52780
