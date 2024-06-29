import requests

url = "http://api.citybik.es/v2/networks"

response = requests.get(url)

if response.status_code == 200:
  data = response.json()
  print(data['networks'][0]["location"])
else:
  print(f"Error: {response.status_code}")