import requests

api_key = "6f5d5df1c61bc00f5d13ef4b3035076a"
city_name = "Patiala"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
