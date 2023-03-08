# Libraries required
import os

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

from src.coffees import IcedCoffee

# Get API key from environment variable, if necessary
# API_KEY = os.environ["API_KEY"]

# Set up API URL and GraphQL query
url = f"https://api.sampleapis.com/coffee/graphql"
query = gql(
"""
query getIcedCoffees {
  allIceds(perPage: 10) {
    title
    id
    description
    ingredients
    image
  }
}
"""
)

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url=url)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Execute the query on the transport
result = client.execute(query)

# Cycle through the response
for coffee in result["allIceds"]:
    print(f"{coffee['title']}: {coffee['description']}")
    print(f"You make this with: {coffee['ingredients']}\n")


# Even better, use a dataclass we setup specifically for 
# this data we imported from the src/coffees.py file.
# Let's use a list comprehension to construct a list of coffees
iced_coffees = [IcedCoffee(**coffee) for coffee in result["allIceds"]]

# Cycle through the response
for coffee in iced_coffees:
    print(f"{coffee.title}: {coffee.description}")
    print(f"You make this with: {coffee.ingredients}\n")
