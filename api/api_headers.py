class APIHeaders:

    @staticmethod
    def default_headers():

        return {

            "Content-Type":
            "application/json",

            "Accept":
            "application/json",

            "x-api-key":
            "free_user_3E8JQZuOoIzzdQ6zpkZL2ETlk4n"
        }
    @staticmethod
    def auth_headers(token):

        headers = (
            APIHeaders.default_headers()
        )

        headers[
            "Authorization"
        ] = f"Bearer {token}"

        return headers