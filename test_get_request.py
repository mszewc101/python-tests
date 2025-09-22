import pytest
from main import get_request, post_request

@pytest.fixture
def response_data():
    return get_request("https://simple-books-api.click")

@pytest.fixture
def response_data_orders():
    return get_request("https://simple-books-api.click/orders")

@pytest.fixture
def response_data_orders_with_auth():
    response = post_request("https://simple-books-api.click/api-clients")
    data = response.json()
    access_token = dict(Authorization = data['accessToken'])
    # {Authorization : d69d69b845d0b8bd634ea0ac01548e9c6b4957a6255f6360fd8893a041641f5f}
    return get_request("https://simple-books-api.click/orders", headers=access_token)

def test_get_request_should_return_200_when_endpoint_is_available(response_data):
    assert response_data.status_code == 200

def test_get_request_should_return_401_when_not_authorized(response_data_orders):
    assert response_data_orders.status_code == 401

def test_get_request_should_return_200_when_authorized(response_data_orders_with_auth):
    assert response_data_orders_with_auth.status_code == 200

