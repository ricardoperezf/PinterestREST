import requests
files = {'file': open('1.jpg', 'rb')}
r = requests.post(url, files=files)
print(r.text)