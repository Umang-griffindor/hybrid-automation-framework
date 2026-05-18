from pages.base_page import BasePage
from utils.config_reader import ConfigReader


class LoginPage(BasePage):

    USERNAME_INPUT = "#username"

    PASSWORD_INPUT = "#password"

    SUBMIT_BUTTON = "#submit"

    SUCCESS_MESSAGE = ".post-title"


    def __init__(self, page):

        super().__init__(page)

        self.config = ConfigReader.read_config()


    def open_login_page(self):

        self.navigate(
            self.config["base_url"]
        )


    def login(self, username, password):

        self.wait_for_element_visible(
        self.USERNAME_INPUT
        )

        self.enter_text(
        self.USERNAME_INPUT,
        username
        )

        self.enter_text(
        self.PASSWORD_INPUT,
        password
        )

        self.click_element(
        self.SUBMIT_BUTTON
        )


    def get_success_message(self):

        return self.get_element_text(self.SUCCESS_MESSAGE)