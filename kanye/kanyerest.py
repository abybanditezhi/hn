import requests
resp = requests.get(url='https://api.kanye.rest')
quote = resp.json()["quote"]
print(quote)