import pytest
import json

TESTDATA={'message': 'elephant'}
TESTDATA_ALPHANUM={'message': 'tat1221tat'}
TESTDATA_NON_ALPHA_NUM={'message': '.tat1221tat.'}

from src.app import create_app
@pytest.fixture
def client():
    """
    testing client for pytest and flask
    """
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_endpoint_response_200(client):
    """
    ensure endpooint returns 200
    """
    rv = client.post("/random_gen_endpoint",json=TESTDATA)
    assert rv.status_code == 200

def test_endpoint_not_alphanumeric(client):
    """
    ensure endpoint returns correct message regarding alphanumeric characters
    """
    rv = client.post("/random_gen_endpoint",json=TESTDATA_NON_ALPHA_NUM)
    resp =  json.loads(rv.data)['message']
    assert resp == 'please only enter alphabetic characters'

def test_endpoint_alphanumeric(client):
    """
    ensure endpoint returns correct message regarding alphanumeric characters
    """
    rv = client.post("/random_gen_endpoint",json=TESTDATA_ALPHANUM)
    resp =  json.loads(rv.data)['message']
    assert resp != 'please only enter alphabetic characters'
    assert 'is a palindrome' in resp