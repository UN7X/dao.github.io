import os
import sys
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app

client = TestClient(app)
HEADERS = {'Authorization': 'Bearer supersecret'}


def test_submit_and_get():
    data = {'hash': 'abc123', 'filename': 'test.txt', 'malware_score': 5}
    resp = client.post('/api/v1/hashcache/submit', json=data, headers=HEADERS)
    assert resp.status_code == 200
    result = resp.json()
    assert result['hash'] == 'abc123'
    resp = client.get('/api/v1/hashcache/abc123', headers=HEADERS)
    assert resp.status_code == 200
    info = resp.json()
    assert 'first_seen' in info and 'last_seen' in info
