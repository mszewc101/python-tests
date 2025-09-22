import pytest
from main import post_request

@pytest.fixture
def response_data():
    return post_request("https://simple-books-api.click/api-clients")

def test_post_request_return_201_when_client_is_created(response_data):
    assert response_data.status_code == 201, f"status code is invalid"
    assert len(response_data.text) == 82, f"len does not match to 82"

    # {"accessToken":"d69d69b845d0b8bd634ea0ac01548e9c6b4957a6255f6360fd8893a041641f5f"}