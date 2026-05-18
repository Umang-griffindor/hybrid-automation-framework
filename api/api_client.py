from multiprocessing.util import get_logger
from utils.logger import get_logger

import requests


class APIClient:

    def get(self, url, headers=None):

        self.logger.info(
            f"Sending GET request to: {url}"
        )

        response = requests.get(
            url,
            headers=headers
        )

        self.logger.info(
            f"Received response: "
            f"{response.status_code}"
        )

        return response


    def post(self, url, payload=None, headers=None):

        self.logger.info(
            f"Sending POST request to: {url}"
        )

        response = requests.post(
            url,
            json=payload,
            headers=headers
        )

        self.logger.info(
            f"Received response: "
            f"{response.status_code}"
        )

        return response
    
    def __init__(self):

        self.logger = get_logger()