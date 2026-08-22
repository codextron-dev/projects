import requests

city = input("Enter city name: ")

api_key = "open weather api key here"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url).json()
print(f"{city}: {response['weather'][0]['description']}, {response['main']['temp']}°C")