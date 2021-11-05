import pytest
from get_doggo import get_doggo

def test_index(app, client):
	res = client.get('/')
	assert res.status_code == 200		# Return's 200 to GET request
	res = client.post('/', data=dict(doggo=''))
	assert res.status_code == 200		# Return's 200 to POST request 

