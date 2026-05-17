from pages.login_page import LoginPage
from utils.config_reader import ConfigReader


config = ConfigReader.read_config()


def test_valid_login(browser_page):

    login_page = LoginPage(browser_page)

    login_page.open_login_page()

    login_page.login(
        config["username"],
        config["password"]
    )

    assert (
        "Logged In Successfully"
        in login_page.get_success_message()
    )