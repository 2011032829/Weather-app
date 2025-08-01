from django.shortcuts import render
import requests

def weather_view(request):
    weather = None
    error = None
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'c6aeb8e977dc87375b53dabc3e6356af'  # Replace with your actual OpenWeatherMap API key
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': data['name'],
                'description': data['weather'][0]['description'].title(),
                'temp': data['main']['temp']
            }
        else:
            error = 'Could not retrieve weather data. Please check the city name.'
    return render(request, 'weather/weather.html', {'weather': weather, 'error': error})
    return render(request, 'weather/weather.html', {'weather': weather, 'error': error})
