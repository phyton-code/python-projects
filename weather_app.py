import requests

API_KEY = "API_KEY_BURAYA"
city = input("Şehir gir: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"

r = requests.get(url)
data = r.json()

if r.status_code == 200:
    print("Şehir:", data["name"])
    print("Sıcaklık:", data["main"]["temp"], "°C")
    print("Hava:", data["weather"][0]["description"])
else:
    print("Hata:", data.get("message"))
