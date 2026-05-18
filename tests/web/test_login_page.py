import pytest

from pages.login_page import LoginPage
from utils.data_reader import DataReader



test_data = DataReader.read_json_data(
    "test_data/login_test_data.json"
)

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.parametrize(
    "data",
    test_data
)
def test_login(page, data):

    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.login(
        data["username"],
        data["password"]
    )

    if data["expected"] == "success":

        success_message = (
            login_page.get_success_message()
        )

        assert (
            "Logged In Successfully"
            in success_message
        )

    else:

        error_message = page.locator(
            "#error"
        ).text_content()

        assert (
            "Your username is invalid!"
            in error_message
        )