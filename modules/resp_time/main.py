import requests
response = requests.get("https://google.com")
print(response.elapsed.total_seconds())
