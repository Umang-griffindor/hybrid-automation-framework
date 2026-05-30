from api.api_client import APIClient

from api.api_headers import APIHeaders


class AuthAPI:

    @staticmethod
    def get_token():

        api_client = APIClient()

        payload = {

            "email":
            "eve.holt@reqres.in",

            "password":
            "cityslicka"
        }

        response, response_time = (

            api_client.post(

                "https://reqres.in/api/login",

            payload=payload,

            headers=
            APIHeaders.default_headers()
        )
    )

        response_data = (
            response.json()
    )

        print(response.status_code)

        print(response_data)

        token = response_data.get(
            "token"
        )

        print(
            f"Generated Token: "
            f"{token}"
        )

        return token