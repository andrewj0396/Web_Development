# Random Doggo!

[Random Doggo Link!](https://doggo.thefamu.net/)

This project in particular just fetches a random dog picture URL from the
random.dog picture api.

[RandomDog API](https://random.dog/woof.json "API for random.dog")

## Install: Linux

```
# virtualenv venv
# source venv/bin/activate
(venv) # pip3 install -r requests.txt
(venv) # python3 __init__.py
```

This project serves as a simple proof of concept Python3 Flask installation.

To run the app locally for testing / dev purposes just enter the python virtual
enviroment and launch the main \_\_init\_\_.py script.

```
# source venv/bin/activate
(venv) # python3 app/__init__.py
```

Then visit `http://127.0.0.1:5000/` in a browser.

Important parts:

* app
* venv
* flaskapp.wsgi

The app/ dir contains the actual flask application.

The venv/ dir contains the python3 virtual enviroment where flask is installed.

The flaskapp.wsgi file is the Web Server Gateway Interface script (sorta like a
special cgi but for Python) that launches our Flask app.

In the apache.conf we have this line in the main site's virtual host block.

`    WSGIScriptAlias / '/var/www/html/flaskapp.wsgi'`

That tells apache to execute the flaskapp.wsgi (python wsgi script) to
bootstrap our Flask application. 

```
from app import app as application
```

Our application is located in the app/ dir. There are three main parts of our
flask app.

* \_\_init\_\_.py
* static
* templates

\_\_init\_\_.py is the main python script for our app. It loads the template for
our index.html file.

```
def index():
	return render_template('index.html')
```

Inside of the app/ dir is also a static/ dir and a templates/ dir.

```
	app
	├── __init__.py
	├── static
	│   └── css
	│       └── main.css
	└── templates
	    ├── base.html
	    └── index.html
```

The app/templates/ dir contains the base.html page that all other site pages
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
that along with a some other jinja sytax to easally modify the base.html page
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

The app/static dir just contains static assests like our css page and images.

