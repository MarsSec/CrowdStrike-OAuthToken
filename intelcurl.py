import requests

# Define the headers
headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6InB1Ym...",
    "Content-Type": "application/json"
}

# Define the URL
url = "https://api.crowdstrike.com/intel/combined/indicators/v1?filter=last_updated:>=1427846400&sort=last_updated|asc"

# Send the GET request
response = requests.get(url, headers=headers)

# Raise an exception if the request was unsuccessful
response.raise_for_status()

# Print the response
print(response.json())
