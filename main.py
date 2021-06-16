
import requests
from datetime import datetime

USER_NAME = "shamimahmed"
TOKEN = "sunday00"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# user_response = requests.post(url=pixela_endpoint, json=user_params)
# print(user_response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "cyclingGraph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# yesterday = datetime(year=2021, month=6, day=15)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kms did you cycle today?\n: "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)


# pixel_data = {
#     "date": yesterday.strftime("%Y%m%d"),
#     "quantity": "9.89",
# }

# update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

# revised_pixel_data = {
#     "quantity": input("How many kms did you cycle yesterday?\n: "),
# }

# response = requests.put(url=update_pixel_endpoint, json=revised_pixel_data, headers=headers)
# print(response.text)

# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)