from api.api_client import APIClient


def test_get_users():

    api_client = APIClient()

    response = api_client.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    assert response.status_code == 200