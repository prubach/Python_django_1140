import requests
from requests.auth import HTTPBasicAuth

url = 'http://localhost:8000/customers/'

response = requests.get(url, auth=HTTPBasicAuth('admin', '123'))
json_data = response.json()
print(json_data)
print(json_data[1]['email'])

newcust = {
    "first_name": "Elsa",
    "last_name": "Smith",
    "email": "elsa@smith.com",
    "birth_date": "2020-11-03"
}

response = requests.post(url, data=newcust, auth=HTTPBasicAuth('admin', '123'))
print(response.json())