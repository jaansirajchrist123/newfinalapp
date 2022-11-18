from django.shortcuts import render

# Create your views here.

import requests

def index(request):
    # https://openweathermap.org/  --Create an account here to get the api key
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=API_KEY' -- we have to give the API_KEY
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9becc482dcf1ab94f64007c8469fcb94'

    city = 'Pune'
    city2 = 'Mumbai'

    city_weather = requests.get(url.format(city)).json() #we are requesting the API data and converting the JSON to Python data types
    print(city_weather) #checking the output

    city_weather2 = requests.get(url.format(city2)).json() #we are requesting the API data and converting the JSON to Python data types
    print(city_weather2) #checking the output


    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon'],

        'city2' : city2,
        'temperature2' : city_weather2['main']['temp'],
        'description2' : city_weather2['weather'][0]['description'],
        'icon2' : city_weather2['weather'][0]['icon']

    }
    return render(request, 'index.html', {'weather' : weather}) #returns the index.html template

    