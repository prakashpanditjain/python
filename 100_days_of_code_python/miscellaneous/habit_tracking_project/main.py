import datetime

import requests

USERNAME = "prakashatpixela"
TOKEN = "abcdefghijklmnopqrstuvwxyz"

pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

# create a graph using POST method
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name": 'coding graph',
    "unit": "programs",
    "type": "int",
    "color": "ajisai",
    "timezone": "Asia/Calcutta",
}

header = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url = graph_endpoint, json=graph_config, headers=header)
# print(response.text)


# This POST requests creates pixels on the graph for a given date
# /v1/users/<username>/graphs/<graphID>
pixela_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": (datetime.datetime.today() - datetime.timedelta(days=40)).strftime('%Y%m%d'),
    "quantity": "2",
}

response = requests.post(url=pixela_endpoint, json=pixel_config, headers=header)
print(response.text)


# PUT method updates the data which you wanna update
graph_update_config = {
    "name": 'python program graph',
    "unit": "programs",
    "color": "sora",
}
# response = requests.put(url=pixela_endpoint, json=graph_update_config, headers=header)
# print(response.text)
