from api.auth import AuthAPI


class APIHeaders:

    @staticmethod
    def default_headers():

        token = AuthAPI.get_token()

        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }