from api.request_builder import (
    RequestBuilder
)

from api.api_client import APIClient

from api.api_headers import (
    APIHeaders
)


def test_request_builder():

    builder = RequestBuilder()

    request_data = (

        builder

        .add_headers(
            APIHeaders.default_headers()
        )

        .add_payload({

            "name":
            "Umang",

            "job":
            "Engineer"
        })

        .build()
    )

    print(request_data)

    api_client = APIClient()

    response = api_client.post(

        "https://reqres.in/api/users",

        payload=
        request_data["payload"],

        headers=
        request_data["headers"]
    )

    print(
        response.json()
    )

    assert (
        response.status_code
        == 201
    )