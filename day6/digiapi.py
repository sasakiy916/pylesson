import requests
import json
import pprint
from googletrans import Translator
url = "https://digimon-api.vercel.app/api/digimon"
jsondata = requests.get(url).json()

translator = Translator()
for dat in jsondata:
    translated = translator.translate(dat["name"], dest="ja")
    print(dat["name"])
    print(translated.text)
    print(dat["img"])
