import requests
import json
response = requests.get('http://localhost:3000/color')
data = response.json()

for widget in data
  print(f"{widget['name']} is {widget['color']}.")
