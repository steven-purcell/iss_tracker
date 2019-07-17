import requests
import json

def get_iss_location():
    res = requests.get('http://api.open-notify.org/iss-now.json')
    content = res.content
    full_response = json.loads(content.decode("utf-8"))
    iss_position = full_response["iss_position"]
    lat = iss_position["latitude"]
    lon = iss_position["longitude"]

    return lat, lon

lat, lon = get_iss_location()

print(lat,', ', lon)

print('https://www.google.com/maps/search/?api=1&query='+str(lat)+','+str(lon)+'&zoom=10&basemap=terrain')
