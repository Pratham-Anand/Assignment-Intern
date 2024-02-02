from django.http import HttpResponse
from django.shortcuts import render,redirect
import requests
from .forms import ContactForm
from django.contrib import messages
from .models import Contact

def index(request):
    return render(request, 'index.html')

def get_weather(request):
    city_name = request.POST.get('city_name')

    if request.method == 'POST' and city_name:
        api_key = "6f5d5df1c61bc00f5d13ef4b3035076a"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(complete_url)
        weather_data = {}

        if response.status_code == 200:
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                weather_data['current_temperature'] = y["temp"]
                weather_data['current_pressure'] = y["pressure"]
                weather_data['current_humidity'] = y["humidity"]
                z = x["weather"]
                weather_data['weather_description'] = z[0]["description"]
            else:
                weather_data['error'] = 'City not found'
        # else:
            # weather_data['error'] = f"API request failed with status code: {response.status_code}"


    else:
        weather_data = {}

    return render(request,'index.html',{'city_name': city_name, 'weather_data': weather_data})


# views.py
# from .forms import ContactForm

def getcontact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully!',extra_tags='success-alert')  # Add success messag
            # Redirect to a success page or another view
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def display(request):
     contacts = Contact.objects.all()
     return render(request, 'display.html', {'contacts': contacts})



    
