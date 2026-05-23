from api.api_client import APIClient
from api.api_headers import APIHeaders


def test_update_user():

    api_client = APIClient()

    payload = {

        "name": "Umang Updated",

        "job": "Senior Automation Engineer"
    }

    response = api_client.put(

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