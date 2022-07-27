# Libraries required
import requests
import os

# Get API key from environment variable
API_KEY = os.environ['PI_KEY']


# Query parameters
param1 = ''
param2 = ''
param3 = ''

# Set up API URL, parameters, and headers
url = f'https://api.example.com/'
params = {
    param1: param1,
    param2: param2,
    param3: param3,
    'key': API_KEY
}
headers = {
    'Accept': 'application/json'
}
response = requests.get(
    url=url, 
    params=params, 
    headers=headers
)
response = response.json()

# Cycle through the response
for x in response:
    
    print(f"{x} is in the data returned.")