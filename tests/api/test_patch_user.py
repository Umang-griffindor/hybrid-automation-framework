from api.api_client import APIClient
from api.api_headers import APIHeaders


def test_patch_user():

    api_client = APIClient()

    payload = {

        "job": "Architect"
    }

    response, response_time = api_client.patch(

        "https://reqres.in/api/users/2",

        payload=payload,

        headers=
        APIHeaders.default_headers()
    )

    print(
        response.json()
    )

    assert (
        response.status_code == 200
    )