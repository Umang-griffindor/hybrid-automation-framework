from playwright.sync_api import expect
from utils.logger import get_logger


class BasePage:

    def __init__(self, page):

        self.page = page
        self.logger = get_logger()


    def navigate(self, url):

        self.logger.info(f"Opening URL: {url}")

        self.logger.info(
            f"Navigating to URL: {url}"
        )

        self.page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

        self.page.wait_for_load_state("networkidle")


    def get_title(self):

        return self.page.title()


    def click_element(self, locator):

        self.logger.info(
            f"Clicking locator: {locator}"
        )

        self.page.locator(locator).click()


    def enter_text(self, locator, text):

        self.logger.info(
            f"Entering text into locator: {locator}"
        )

        self.page.locator(locator).fill(text)


    def wait_for_element(self, locator):

        self.page.locator(locator).wait_for(state="visible")


    def is_element_visible(self, locator):

        return self.page.locator(locator).is_visible()


    def get_element_text(self, locator):

        self.logger.info(
            f"Getting text from locator: {locator}"
        )

        return self.page.locator(locator).text_content()


    def expect_element_visible(self, locator):

        expect(self.page.locator(locator)).to_be_visible()

    def wait_for_element_visible(
        self,
        locator,
        timeout=30000
        ):

        self.logger.info(
        f"Waiting for element visibility: "
        f"{locator}"
        )

        self.page.locator(locator).wait_for(
        state="visible",
        timeout=timeout
        )
    
    def wait_for_element_hidden(
        self,
        locator,
        timeout=30000
        ):

        self.logger.info(
        f"Waiting for element hidden: "
        f"{locator}"
        )

        self.page.locator(locator).wait_for(
        state="hidden",
        timeout=timeout
        )

    def wait_for_text(
        self,
        locator,
        text,
        timeout=30000
        ):

        self.logger.info(
        f"Waiting for text '{text}' "
        f"in locator: {locator}"
        )

        self.page.locator(locator).wait_for(
        timeout=timeout
        )

        assert (
        text in
        self.page.locator(locator).text_content()
        )