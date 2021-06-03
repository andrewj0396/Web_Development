import requests, json
from bs4 import BeautifulSoup

url = "https://random.dog/woof.json"

s = requests.Session()
g = s.get(url)
doggo_json = json.loads(g.text)
print(doggo_json["url"])

"""
r_html = g.text

if g.status_code == 200:
	print("page got")
else:
	print("Failed")
	exit(1)

print(r_html)
"""
