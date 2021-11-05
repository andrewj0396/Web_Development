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
