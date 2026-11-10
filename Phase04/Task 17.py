
import requests

# Use a placeholder token, not a real credential
token = "YOUR_TOKEN_HERE"

url = "https://httpbin.org/get"

# Construct the Authorization header
headers = {
    "Authorization": f"Bearer {token}"
}

# Print sanitized request configuration
print("HTTP Method: GET")
print("Endpoint:", url)
print("Request Headers:")

sanitized_headers = headers.copy()
sanitized_headers["Authorization"] = "Bearer <TOKEN_REDACTED>"

print(sanitized_headers)

# Construct the request (no real credential is used)
request = requests.Request(
    method="GET",
    url=url,
    headers=headers
)

prepared_request = request.prepare()

print("\nPrepared Request Configuration:")
print("Method:", prepared_request.method)
print("URL:", prepared_request.url)
print("Authorization Header Format:",
      "Bearer <TOKEN_REDACTED>")
