from api.api_client import APIClient  # import reusable API client for HTTP requests
from api.api_headers import APIHeaders  # import standard API headers helper
from api.response_validator import ResponseValidator  # import response validation helpers


def test_create_post():  # pytest test function for creating a post against a public API

    api_client = APIClient()  # instantiate API client wrapper

    payload = {
        "title": "Playwright Framework",
        "body": "Learning API Automation",
        "userId": 1
    }  # JSON payload representing a new post

    response, response_time = api_client.post(
        "https://jsonplaceholder.typicode.com/posts",
        payload=payload,
        headers=APIHeaders.default_headers()
    )  # send POST request and capture response data

    response_data = response.json()  # convert JSON response into Python object

    ResponseValidator.validate_status_code(
        response,
        201
    )  # assert that the API returned HTTP 201 Created

    ResponseValidator.validate_json_key(
        response_data,
        "title"
    )  # assert that the expected title field exists in the response JSON