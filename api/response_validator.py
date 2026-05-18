class ResponseValidator:  # Python class for reusable API response assertions

    @staticmethod  # static method syntax because validation does not require object state
    def validate_status_code(response, expected_status):  # method to verify HTTP status codes

        assert (
            response.status_code == expected_status
        ), (
            f"Expected status code "
            f"{expected_status}, "
            f"but got {response.status_code}"
        )  # assertion ensures the API returned the expected status, aiding fast failure in tests


    @staticmethod  # static method for JSON key validation
    def validate_json_key(response_data, key):  # method checks required keys exist in JSON payloads

        assert key in response_data, (
            f"Key '{key}' not found in response"
        )  # assertion provides a clear failure message when response structure is wrong