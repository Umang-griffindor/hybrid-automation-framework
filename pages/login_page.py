from pages.base_page import BasePage  # import base page class containing common Playwright actions
from utils.config_reader import ConfigReader  # import config reader to load base_url and other settings


class LoginPage(BasePage):  # Python page object model class for login page actions

    USERNAME_INPUT = "#username"  # class-level selector constant for the username field

    PASSWORD_INPUT = "#password"  # class-level selector constant for the password field

    SUBMIT_BUTTON = "#submit"  # class-level selector constant for the submit button

    SUCCESS_MESSAGE = ".post-title"  # class-level selector constant used to verify successful login


    def __init__(self, page):  # constructor accepts a Playwright Page object

        super().__init__(page)  # call base page constructor to initialize shared helpers

        self.config = ConfigReader.read_config()  # load environment config once per page object


    def open_login_page(self):  # method navigates to the login page URL

        self.navigate(
            self.config["base_url"]
        )  # use the base page navigate helper with URL from config


    def login(self, username, password):  # method fills login form and submits it

        self.wait_for_element_visible(
            self.USERNAME_INPUT
        )  # ensure username input is visible before interacting

        self.enter_text(
            self.USERNAME_INPUT,
            username
        )  # fill the username using the reusable base page helper

        self.enter_text(
            self.PASSWORD_INPUT,
            password
        )  # fill the password field using base page helper

        self.safe_click(
            self.SUBMIT_BUTTON
        )  # safely click submit after waiting for visibility


    def get_success_message(self):  # method retrieves the login success message text

        return self.get_element_text(self.SUCCESS_MESSAGE)  # reuse base page text extraction helper
    