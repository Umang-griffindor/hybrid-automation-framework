from api.api_client import APIClient
from api.api_headers import APIHeaders
from api.response_validator import ResponseValidator


def test_create_post():

    api_client = APIClient()

    payload = {
        "title": "Playwright Framework",
        "body": "Learning API Automation",
        "userId": 1
    }

    response = api_client.post(
        "https://jsonplaceholder.typicode.com/posts",
        payload=payload,
        headers=APIHeaders.default_headers()
    )

    response_data = response.json()

    ResponseValidator.validate_status_code(
        response,
        201
    )

    ResponseValidator.validate_json_key(
        response_data,
        "title"
    )