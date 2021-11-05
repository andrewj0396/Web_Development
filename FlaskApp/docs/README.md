# Random Doggo!

[See Random Doggo Site in Action!](https://doggo.thefamu.net/)

This project in particular just fetches a random dog picture URL from the
[Random.Dog API](https://random.dog/woof.json "API for random.dog").

## Install Project & Python Dependencies

```
git clone https://github.com/BlueSquare23/Web_Development.git
cd Web_Development/FlaskApp/
virtualenv venv			# Virtual Env Optional
source venv/bin/activate	# Virtual Env Optional
pip3 install -r requirements.txt
```

## Running the Project Locally

This project serves as a simple proof of concept Python3 Flask installation.

To run the app locally for testing / dev purposes just enter the python virtual
environment and launch the main `app.py` script.

```
cd FlaskApp
source venv/bin/activate	# Virtual Env Optional
python3 app.py
```

Then visit `http://127.0.0.1:5000/` in a browser.

## Running the Project on a Server

You'll need a
[WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) compatible
web server in order to run this FlaskApp. In my case, I'm using an Apache web
server running `mod_wsgi`.

The `flaskapp.wsgi` file is the WSGI script (sorta like a Pythonic version of
CGI) that launches our Flask app.

In the apache.conf we have this line in the main site's virtual host block.

`    WSGIScriptAlias / '/var/www/html/flaskapp.wsgi'`

That tells Apache to execute the flaskapp.wsgi (Python WSGI script) to import
and run our Flask application. 

```
from website import run_app
application = run_app()
```

## Project Structure

#### App Overview:

Our application is located in the website/ dir. There are three main parts of our
flask app.

* \_\_init\_\_.py
* index.py
* get\_doggo.py
* static
* templates

\_\_init\_\_.py is the main python script for our app. It loads our main routes
for the site, such as the index and reload routes.

```
from website.index import index
app.register_blueprint(index, url_prefix="/")
```

Our index route itself is defined in `index.py`. The site's main index route
works by importing the `get_doggo()` fucntion from `get_doggo.py` and then uses
the returned doggo to render the index page.

```
from website.get_doggo import get_doggo

...

@index.route('/', methods=['POST', 'GET'])

def home():
	doggo_url = get_doggo()
	return render_template('index.html', doggo=doggo_url)
```

Inside of the website/ dir is also a static/ dir and a templates/ dir.

```
	website
	├── static
	│   └── css
	│       └── main.css
	└── templates
	    ├── base.html
	    └── index.html
```

The website/templates/ dir contains the base.html page that all other site pages
are based off of.

```
<!doctype html>
<html>
<head>
	{% block head %}{% endblock %}
	<meta name="description" content="My first page">
	<meta name="keywords" content="html python template">
	<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
</head>

<body>
	{% block body %}{% endblock %}
</body>
```

As you can see that page contains Jinja 2 syntax for templating. We can use
that along with a some other jinja sytax to easily modify the base.html page
into new pages.

For example, here's the only contents of index.html.

```
{% extends 'base.html' %}

{% block head %}
<title>First Flask Site</title>
{% endblock %}

{% block body %}
<h1>Hello World!</h1>
{% endblock %}
```

All that's needed to extend the page is add some Jinja syntax at the top of a
new page.

The website/static dir just contains static assets like our css page and images.

