class ResponseValidator:

    @staticmethod
    def validate_status_code(response, expected_status):

        assert (
            response.status_code == expected_status
        ), (
            f"Expected status code "
            f"{expected_status}, "
            f"but got {response.status_code}"
        )


    @staticmethod
    def validate_json_key(response_data, key):

        assert key in response_data, (
            f"Key '{key}' not found in response"
        )