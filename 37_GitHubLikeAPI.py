import requests

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "adissuu"
TOKEN = "jfirwej431ngm2134"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url = pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "adi1",
    "name": "Booking Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{graph_params['id']}"
print(pixel_endpoint)
import datetime
now = datetime.datetime.now()
year = str(now.year)
month = str(now.month)
if int(month) < 10:
    month = "0"+month
day = str(now.day)
if int(day) < 10:
    day = "0"+day
date = year+month+day

quantity = input("Enter the number of pages read today: ")

pixel_params = {
    "date": date,
    "quantity": quantity,
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)