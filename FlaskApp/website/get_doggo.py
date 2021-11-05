import requests
import json

def get_doggo():
	# Random.dog API Woof.json URL
	url = "https://random.dog/woof.json"

	s = requests.Session()
	g = s.get(url)

	doggo_json = json.loads(g.text)
	doggo_url = doggo_json["url"]
	doggo_size = doggo_json["fileSizeBytes"]

	# If the img is larger than 3mb,
	if doggo_size > 3000000:
		# Recurse and get new doggo pic
		doggo_url = get_doggo()

	# Or if the link is to an mp4 / webm video,
	if "mp4" in doggo_url or "webm" in doggo_url:
		# Recurse and get new doggo pic
		doggo_url = get_doggo()
	
	# If all good, return image link
	return doggo_url
