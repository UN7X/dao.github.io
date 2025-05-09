import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get('/api/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'ok'
    assert 'message' in json_data

def test_get_items(client):
    response = client.get('/api/items')
    assert response.status_code == 200
    json_data = response.get_json()
    assert isinstance(json_data, list)
    assert len(json_data) > 0

def test_get_single_item(client):
    response = client.get('/api/items/1')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['id'] == 1
    assert 'name' in json_data

def test_create_item(client):
    test_item = {'name': 'Test Item', 'description': 'This is a test'}
    response = client.post('/api/items', json=test_item)
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['success'] is True
    assert json_data['item']['name'] == 'Test Item'