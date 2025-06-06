import os
import sys
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app

client = TestClient(app)
HEADERS = {'Authorization': 'Bearer supersecret'}


def test_locker_crud():
    # create locker
    res = client.post('/api/v1/asix/lockers', json={}, headers=HEADERS)
    assert res.status_code == 200
    locker_id = res.json()['id']
    # add object
    obj = {'data': {'foo': 'bar'}}
    res = client.post(f'/api/v1/asix/lockers/{locker_id}/objects', json=obj, headers=HEADERS)
    assert res.status_code == 200
    obj_id = res.json()['id']
    # read object
    res = client.get(f'/api/v1/asix/lockers/{locker_id}/objects/{obj_id}', headers=HEADERS)
    assert res.status_code == 200
    assert res.json()['data']['foo'] == 'bar'
