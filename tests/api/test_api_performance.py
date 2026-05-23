from api.api_client import APIClient

from api.api_headers import APIHeaders

from api.api_assertions import (
    APIAssertions
)


def test_api_response_time():

    api_client = APIClient()

    response, response_time = (

        api_client.get(

            "https://reqres.in/api/users/2",

            headers=
            APIHeaders.default_headers()
        )
    )

    APIAssertions.verify_status_code(
        response,
        200
    )

    APIAssertions.verify_response_time(

        response_time,

        3
    )