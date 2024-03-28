import requests
import json
import win32com.client as wincom

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
x = wdic["location"]["country"]
y = wdic["location"]["region"]
z = wdic["location"]["name"]

print(f'City:{z}')
print(f'Country:{x}')
print(f'Region:{y}')
print(f'Temperature:{w}°C')

speak = wincom.Dispatch("SAPI.SpVoice")
speak.speak(f'The temperature of {city} is {w} °C')
s = "Thank you....Have a nice day!"
print(s)
speak.speak(s)

