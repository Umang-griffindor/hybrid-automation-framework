import pytest  # import pytest for marker and parametrized test syntax

from pages.login_page import LoginPage  # import page object for login flow actions
from utils.data_reader import DataReader  # import data reader for structured test data



test_data = DataReader.read_json_data(
    "test_data/login_test_data.json"
)  # load JSON-driven test cases for data-driven UI validation

@pytest.mark.ui  # pytest marker to categorize this test as UI automation
@pytest.mark.smoke  # pytest marker to classify this test as smoke test coverage
@pytest.mark.parametrize(
    "data",
    test_data
)  # pytest parametrize syntax to run the same test for multiple data sets
def test_login(page, data):  # Playwright test that performs login functionality checks

    login_page = LoginPage(page)  # instantiate login page object with the Playwright page

    login_page.open_login_page()  # navigate to the login page URL from config

    login_page.login(
        data["username"],
        data["password"]
    )  # perform login with username and password from test data

    if data["expected"] == "success":  # conditional branch for expected success scenario

        success_message = (
            login_page.get_success_message()
        )  # get the success message text from the page object

        assert (
            "Logged In Successfully"
            in success_message
        )  # assert statement verifies successful login text is present

    else:  # branch for expected failure scenario

        error_message = page.locator(
            "#error"
        ).text_content()  # Playwright locator gets error message content

        assert (
            "Your username is invalid!"
            in error_message
        )  # verify error message appears for invalid credentials