# Libraries required
from ast import literal_eval
import os

import requests

from src.coffees import IcedCoffee

# Get API key from environment variable, if necessary
# API_KEY = os.environ["API_KEY"]

# Query parameters, if needed
# param1 = ""
# param2 = ""
# param3 = ""
# param4 = ""

# params = {
#     param1: param1,
#     param2: param2,
#     param3: param3,
#     param4: param4,
#     "key": API_KEY,
# }

# Set up API URL and headers
url = f"https://api.sampleapis.com/coffee/iced"
headers = {"Accept": "application/json"}

response = requests.get(url=url, headers=headers)
data: dict = response.json()

# Cycle through the response
for coffee in data:
    print(f"{coffee['title']}: {coffee['description']}")
    print(f"You make this with: {coffee['ingredients']}\n")


# Even better, use a dataclass we setup specifically for 
# this data we imported from the src/coffees.py file.
# Let's use a list comprehension to construct a list of coffees
iced_coffees = [IcedCoffee(**coffee) for coffee in data]

# Cycle through the response
for coffee in iced_coffees:
    print(f"{coffee.title}: {coffee.description}")
    print(f"You make this with: {coffee.ingredients}\n")
