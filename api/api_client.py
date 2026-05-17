import requests


class APIClient:

    def get(self, url, headers=None):

        response = requests.get(
            url,
            headers=headers
        )

        return response


    def post(self, url, payload=None, headers=None):

        response = requests.post(
            url,
            json=payload,
            headers=headers
        )

        return response