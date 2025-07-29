# pip install requests pywin32
import requests
import json
import win32com.client as wincom
import time

city = input("Enter the name of the city:\n")

api_key = "a9d25a5b02ea4ea7bc9124252252907"
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

r = requests.get(url)
# print(r.text)
# print(type(r.text))
weatherdic = json.loads(r.text)
w = weatherdic["current"]["temp_c"]


# you can insert gaps in the narration by adding sleep calls

speak = wincom.Dispatch("SAPI.SpVoice")

text = f"The current weather in {city} is {w} degrees"
speak.Speak(text)

# New text will be read after 2 seconds
time.sleep(2) 

text = "Thank you for your patience"
speak.Speak(text)