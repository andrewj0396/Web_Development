import pytest
from get_doggo import get_doggo

def test_get_doggo():
	assert type(get_doggo()) is str		# Is string
	assert 'random.dog' in get_doggo() 	# Contains 'random.dog' substring
	assert len(get_doggo()) < 70		# Length less than 70 chars
	assert 'webm' not in get_doggo()	# Does not contain 'webm' substring
	assert 'mp4' not in get_doggo()		# Does not contain 'mp4' substring

