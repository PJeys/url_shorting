import requests

url = 'http://127.0.0.1:5000/'
resp = requests.get('http://127.0.0.1:5000/api/v1/get_short/?url=url.com')
print(resp.json())