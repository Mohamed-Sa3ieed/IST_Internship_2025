import requests

# Create a session to persist cookies
session = requests.Session()

# Set the cookie directly in the session's cookie jar
url = "http://127.0.0.1:8000/items"
session.cookies.set('ads_id', '123458')

# Make the GET request using the session
response = session.get(url)

# Print the response
print(response.text)