from jsonschema import validate

from api.api_client import APIClient

from api.api_headers import APIHeaders

from schemas.user_schema import (
    user_schema
)
from api.api_assertions import (
    APIAssertions
)

def test_user_schema():

    api_client = APIClient()

    response, response_time = api_client.get(

        "https://reqres.in/api/users/2",

        headers=
        APIHeaders.default_headers()
    )

    response_data = (
        response.json()
    )

    print(response_data)

    validate(

        instance=response_data,

        schema=user_schema
    )

    APIAssertions.verify_status_code(
        response,
        200
    )

    APIAssertions.verify_key_present(
        response_data,
        "data"
    )