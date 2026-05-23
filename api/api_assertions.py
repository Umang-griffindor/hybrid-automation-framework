class APIAssertions:

    @staticmethod
    def verify_status_code(
        response,
        expected_status
    ):

        actual_status = (
            response.status_code
        )

        assert (
            actual_status
            == expected_status
        ), (

            f"Expected status "
            f"{expected_status}, "

            f"but got "
            f"{actual_status}"
        )

    @staticmethod
    def verify_key_present(
        response_data,
        key
    ):

        assert (
            key in response_data
        ), (

            f"Key '{key}' "
            f"not found in response"
        )

    @staticmethod
    def verify_value(
        actual,
        expected
    ):

        assert (
            actual == expected
        ), (

            f"Expected '{expected}' "

            f"but got '{actual}'"
        )

    @staticmethod
    def verify_response_time(
        response_time,
        max_time
    ):

        assert (
            response_time <= max_time
        ), (

            f"Response time "
            f"{response_time:.2f}s "

            f"exceeded limit "
            f"{max_time}s"
        )