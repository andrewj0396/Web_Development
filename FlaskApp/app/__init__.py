from flask import Flask, render_template, request, redirect
import requests # request and requests are different 
import json

# Our app is this file
app = Flask(__name__)

# Webroot is '/'
@app.route('/', methods=['POST', 'GET'])

# Index page contents
def index():
	doggo_url = get_doggo()
	return render_template('index.html', doggo=doggo_url)


def get_doggo():
	url = "https://random.dog/woof.json"

	s = requests.Session()
	g = s.get(url)

	doggo_json = json.loads(g.text)
	doggo_url = doggo_json["url"]

	if "mp4" in doggo_url or "webm" in doggo_url:
		doggo_url = get_doggo()

	return doggo_url


# Run the app, w/ debug
if __name__ == "__main__":
	app.run(debug=False)

