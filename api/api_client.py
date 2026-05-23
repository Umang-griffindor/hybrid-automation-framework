import requests
import time
from utils.logger import get_logger


class APIClient:

    def __init__(self):

        self.logger = get_logger()

    def get(
        self,
        url,
        headers=None,
        params=None
    ):

        self.logger.info(
            f"GET Request URL: {url}"
        )

        self.logger.info(
            f"Request Headers: {headers}"
        )

        self.logger.info(
            f"Request Params: {params}"
        )

        start_time = time.time()

        response = requests.get(

            url,

            headers=headers,

            params=params
        )

        end_time = time.time()

        response_time = (
            end_time - start_time
        )

        self.logger.info(
            f"Response Status: "
            f"{response.status_code}"
        )

        self.logger.info(
            f"Response Body: "
            f"{response.text}"
        )

        self.logger.info(
            f"Response Time: "
            f"{response_time:.2f} seconds"
        )

        return response, response_time

    def post(
        self,
        url,
        payload=None,
        headers=None
    ):

        self.logger.info(
        f"POST Request URL: {url}"
        )

        self.logger.info(
        f"Request Headers: {headers}"
        )

        self.logger.info(
        f"Request Payload: {payload}"
        )

        start_time = time.time()

        response = requests.post(

        url,

        json=payload,

        headers=headers
        )

        end_time = time.time()

        response_time = (
            end_time - start_time
        )

        self.logger.info(
            f"Response Time: "
            f"{response_time:.2f} seconds"
        )

        self.logger.info(
        f"Response Status: "
        f"{response.status_code}"
        )

        self.logger.info(
        f"Response Body: "
        f"{response.text}"
        )

        return response, response_time

    def put(
        self,
        url,
        payload=None,
        headers=None
    ):

        self.logger.info(
            f"PUT Request URL: {url}"
        )

        self.logger.info(
            f"Request Headers: {headers}"
        )

        self.logger.info(
            f"Request Payload: {payload}"
        )

        start_time = time.time()

        response = requests.put(

            url,

            json=payload,

            headers=headers
        )

        end_time = time.time()

        response_time = (
            end_time - start_time
        )

        self.logger.info(
            f"Response Status: "
            f"{response.status_code}"
        )

        self.logger.info(
            f"Response Body: "
            f"{response.text}"
        )

        self.logger.info(
            f"Response Time: "
            f"{response_time:.2f} seconds"
        )

        return response, response_time

    def patch(
        self,
        url,
        payload=None,
        headers=None
    ):

        self.logger.info(
            f"PATCH Request URL: {url}"
        )

        self.logger.info(
            f"Request Headers: {headers}"
        )

        self.logger.info(
            f"Request Payload: {payload}"
        )

        start_time = time.time()

        response = requests.patch(

            url,

            json=payload,

            headers=headers
        )

        end_time = time.time()

        response_time = (
            end_time - start_time
        )

        self.logger.info(
            f"Response Status: "
            f"{response.status_code}"
        )

        self.logger.info(
            f"Response Body: "
            f"{response.text}"
        )

        self.logger.info(
            f"Response Time: "
            f"{response_time:.2f} seconds"
        )

        return response, response_time

    def delete(
        self,
        url,
            headers=None
    ):

        self.logger.info(
            f"DELETE Request URL: {url}"
        )

        self.logger.info(
            f"Request Headers: {headers}"
        )

        start_time = time.time()

        response = requests.delete(

            url,

            headers=headers
        )

        end_time = time.time()

        response_time = (
            end_time - start_time
        )

        self.logger.info(
            f"Response Status: "
            f"{response.status_code}"
        )

        self.logger.info(
            f"Response Body: "
            f"{response.text}"
        )

        self.logger.info(
            f"Response Time: "
            f"{response_time:.2f} seconds"
        )

        return response, response_time