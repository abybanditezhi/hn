print("ass")
import requests
print("asss")
resp = requests.get(url='https://api.kanye.rest')
quote = resp.json()["quote"]
print(quote)