import requests
import json

# Replace with your actual client ID and client secret
client_id = ""
client_secret = ""

# CrowdStrike OAuth2 endpoint and Intel API endpoint
token_url = "https://api.crowdstrike.com/oauth2/token"
api_url = "https://api.crowdstrike.com/intel/entities/indicators/GET/v1"

# Request the bearer token
auth_response = requests.post(
    token_url,
    data={
        "client_id": client_id,
        "client_secret": client_secret,
    },
)

# Raise an exception if the request was unsuccessful
auth_response.raise_for_status()

# Extract the bearer token from the response
bearer_token = auth_response.json()["access_token"]

# Use the bearer token to make a GET request to the API
api_response = requests.get(
    api_url,
    headers={
        "Authorization": f"Bearer {bearer_token}",
    },
)

ids = ["hash_md5_86AA695AD63192A4F5DE5D5B0F64F326", "hash_sha1_d61ee0b0d4ed95f3300735c81740a21b8beef337", "hash_sha1_86092636e7ffa22481ca89ac1b023c32c56b24cf"]

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}

# The body of the request
data = {
    "ids": ids
}

# Send a POST request to the API
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# Raise an exception if the request was unsuccessful
response.raise_for_status()

# Get the response data as a Python object
data = response.json()

# Now, let's write this data to a file
with open('indicators.txt', 'w') as f:
    f.write(json.dumps(data, indent=4))
