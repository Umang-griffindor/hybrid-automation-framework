from api.api_client import APIClient
from api.api_headers import APIHeaders


def test_delete_user():

    api_client = APIClient()

    response, response_time = api_client.delete(

        "https://reqres.in/api/users/2",

        headers=
        APIHeaders.default_headers()
    )

    assert (
        response.status_code == 204
    )