from api.auth import AuthAPI  # import auth helper from the API auth module


class APIHeaders:  # Python class grouping API header helper methods

    @staticmethod  # static method syntax since no instance state is needed
    def default_headers():  # method returns the standard headers used for API requests

        token = AuthAPI.get_token()  # get a reusable token to add into Authorization header

        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }  # return Python dict used by APIClient for authenticated JSON calls