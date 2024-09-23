import pytest
from app import app
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_getcode(client):
    response = client.get('/getcode')
    assert response.status_code == 200
    assert response.json['message'] == "Hello, World!"

def test_plus(client):
    response = client.get('/plus/5/6')
    assert response.status_code == 200
    assert response.json['result'] == 11