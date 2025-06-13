from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    city = request.GET.get('city')
    api_key = "3a667663cbd78f06f5e644cd1c3ee9b3"
    api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    print(api_url)
    api=requests.get(api_url).json()

    temperature = api['main']['temp']
    city=api['name']
    country=api['sys']['country']

    return render(request,'INDEX.HTML',{'temperature':temperature ,'city':city , 'country':country})
