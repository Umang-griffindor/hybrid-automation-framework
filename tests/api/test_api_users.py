from api.api_client import APIClient
from api.api_headers import APIHeaders
from api.response_validator import ResponseValidator
from utils.config_reader import ConfigReader


def test_create_post():

    config = ConfigReader.read_config()

    api_client = APIClient()

    payload = {
        "title": "Playwright Framework",
        "body": "Learning API Automation",
        "userId": 1
    }

    response = api_client.post(
        f"{config['api_base_url']}/posts",
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