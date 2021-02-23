import requests
import json

r = requests.get("https://restcountries.eu/rest/v2/region/europe")
data = r.json()
for name in data:
    print(name['region']+"/"+name['subregion'])
