import os
import sys
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get('/api/v1/timestamped/health', headers={'Authorization': 'Bearer supersecret'})
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'


def test_timestamp_endpoint():
    response = client.post(
        '/api/v1/timestamped/timestamp',
        json={'content': 'hello'},
        headers={'Authorization': 'Bearer supersecret'}
    )
    assert response.status_code == 200
    assert 'timestamp' in response.json()
