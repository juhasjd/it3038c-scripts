import requests
import json
response = requests.get('http://localhost:3000/color')
data = response.json()

print(f"{widget['name']} is {widget['color']}.")
