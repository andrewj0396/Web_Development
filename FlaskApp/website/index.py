from flask import Flask, render_template, Blueprint
from website.get_doggo import get_doggo

index = Blueprint("index", __name__)

# Webroot is just '/'
@index.route('/', methods=['POST', 'GET'])

# Index page contents
def home():
	doggo_url = get_doggo()
	return render_template('index.html', doggo=doggo_url)
