
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "My API Lab",
    "body": "Testing POST request",
    "userId": 1
}

response = requests.post(url, json=data)

print("HTTP Method: POST")
print("Endpoint:", url)
print("Request Body:")
print(json.dumps(data, indent=2))
print("Status Code:", response.status_code)
print("Response Body:")
print(json.dumps(response.json(), indent=2))
