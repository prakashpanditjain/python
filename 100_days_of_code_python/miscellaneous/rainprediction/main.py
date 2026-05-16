import os

api_key = os.environ.get('WAK')
end_point = "http://api.openweathermap.org/data/2.5/forecast"

parameter = {
    'lat' : 18.4,
    'lon' : 76.56,
    'appid' : api_key,
    'cnt' : 4
}

import requests

response = requests.get(end_point, params=parameter)
# print(response.json())
response.raise_for_status()
weather_data = response.json()['list']
weather_id = ["Bring an Umbrella" if weather_data[i]['weather'][0]['id']< 700 else "No need for an Umbrella, It will not rain" for i in range(len(weather_data)) ]
print((weather_id))


