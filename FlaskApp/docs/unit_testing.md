# Flask Unit Testing

## Overview

I've set up very basic unit testing for the doggo bot project using Python
Pytest module. The testing structure looks like this. 

Testing Structure:

	testing/
	├── conftest.py
	├── test_get_doggo.py
	└── test_index.py

### Conftest.py

First, there's a conftest.py file used for initializing the flask WSGI server
when the tests are run. This script starts the application and sets up a
test\_client() that can be used to access the app.

Conftest.py File:

	import sys
	import pytest
	from website import run_app

	app_path='website'
	sys.path.insert(0, app_path)

	application = run_app()

	@pytest.fixture
	def app():
	    yield application

	@pytest.fixture
	def client(app):
	    return app.test_client()

### Unit Test Files

Then there are the actual unit files we'll be testing. We'll be testing each
function from each file independently.

Main Functions to Test:

	def index():
	def doggo():
	def get_doggo():

The second part of this all are the test files themselves, named
test\_\_UNIT\_FILE\_NAME.py as per Pytest's naming conventions. They contain the
actual test code that will be run against the flask application.

## Sample Test Case

	def test_index(app, client):
		res = client.get('/')
		assert res.status_code == 200		# Return's 200 to GET request

If all of the test functions within the test\_\_UNIT\_FILE\_NAME.py files return
true then the tests are successful. However, if any of them fail the whole
Pytest returns false.

To run the test is simple:
	
	cd FlaskApp 
	python3 -m pytest 

The link below contains a simple test setup for a Python Flask app for
reference.

[Flask Pytest Example](https://dev.to/po5i/how-to-add-basic-unit-test-to-a-python-flask-app-using-pytest-1m7a)

