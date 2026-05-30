from api.api_client import APIClient  # import HTTP client wrapper used for API calls
from api.api_headers import APIHeaders  # import helper for default headers and authentication
from api.response_validator import ResponseValidator  # import reusable assertions for API responses
from utils.config_reader import ConfigReader  # import config reader to load API endpoint settings


def test_create_post():  # pytest test function that validates creating a new post via API

    config = ConfigReader.read_config()  # load environment-specific configuration settings

    api_client = APIClient()  # create an instance of the API client wrapper

    payload = {
        "title": "Playwright Framework",
        "body": "Learning API Automation",
        "userId": 1
    }  # Python dict payload used for the API POST body

    response, response_time = api_client.post(
        f"{config['api_base_url']}/posts",
        payload=payload,
        headers=APIHeaders.default_headers()
    )  # send POST request and capture the HTTP response

    response_data = response.json()  # parse the JSON response into a Python dict

    ResponseValidator.validate_status_code(
        response,
        201
    )  # validate that the response HTTP status is 201 Created

    ResponseValidator.validate_json_key(
        response_data,
        "title"
    )  # validate that the returned response contains the expected JSON key