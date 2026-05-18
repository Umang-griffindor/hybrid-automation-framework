from utils.logger import get_logger  # Python import of custom logger helper for framework logging

import requests  # Python import of requests library for HTTP API calls


class APIClient:  # Python class that wraps API request behavior for reuse

    def __init__(self):  # Python constructor initializes the reusable logger instance

        self.logger = get_logger()  # create a logger from utils.logger for request tracing

    def get(self, url, headers=None):  # method syntax for sending HTTP GET requests

        self.logger.info(
            f"Sending GET request to: {url}"
        )  # logger call records the outgoing request URL

        response = requests.get(
            url,
            headers=headers
        )  # requests library call performs the GET request

        self.logger.info(
            f"Received response: "
            f"{response.status_code}"
        )  # logger call records the response status code for debugging

        return response  # return statement makes the HTTP response available to tests


    def post(self, url, payload=None, headers=None):  # method syntax for sending HTTP POST requests

        self.logger.info(
            f"Sending POST request to: {url}"
        )  # log the outgoing POST URL

        response = requests.post(
            url,
            json=payload,
            headers=headers
        )  # requests call sends JSON payload and optional headers

        self.logger.info(
            f"Received response: "
            f"{response.status_code}"
        )  # log the returned status code for validation

        return response  # return the response object to the calling test or helper