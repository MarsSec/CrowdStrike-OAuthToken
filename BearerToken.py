import requests

# Replace with your actual client ID and client secret
client_id = "Add Here"
client_secret = "Add Here"

# URL for your token request endpoint
token_url = "https://api.crowdstrike.com/oauth2/token"  # replace with your actual token URL

# Send a POST request to the token endpoint
response = requests.post(
    token_url,
    data={
        "client_id": client_id,
        "client_secret": client_secret,
    },
)

# Raise an exception if the request was unsuccessful
response.raise_for_status()

# Extract the bearer token from the response
bearer_token = response.json()["access_token"]

print("Bearer token: ", bearer_token)
