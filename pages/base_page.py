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

    def wait_for_response(
        self,
        trigger_action,
        url_part,
        timeout=30000
    ):

        self.logger.info(
        f"Waiting for response containing: "
        f"{url_part}"
        )

        with self.page.expect_response(
        lambda response:
        url_part in response.url,
        timeout=timeout
        ) as response_info:

            trigger_action()

        return response_info.value
    
    def wait_for_spinner_to_disappear(
        self,
        spinner_locator,
        timeout=30000
    ):

        self.logger.info(
            f"Waiting for spinner to disappear: "
            f"{spinner_locator}"
        )

        self.page.locator(
            spinner_locator
        ).wait_for(
            state="hidden",
            timeout=timeout
        )

    def safe_click(
        self,
        locator,
        timeout=30000
    ):

        self.wait_for_element_visible(
            locator,
            timeout
        )

        self.logger.info(
            f"Safely clicking element: "
            f"{locator}"
        )

        self.page.locator(locator).click()

    def get_frame_locator(
        self,
        frame_locator
    ):

        self.logger.info(
            f"Switching to iframe: "
            f"{frame_locator}"
        )

        return self.page.frame_locator(
            frame_locator
        )
    
    def get_shadow_locator(
        self,
        parent_locator,
        child_locator
    ):

        self.logger.info(
            f"Accessing shadow DOM element: "
            f"{child_locator}"
        )

        return self.page.locator(
            parent_locator
        ).locator(
            child_locator
        )
    
    def wait_for_new_tab(
        self,
        trigger_action
    ):

        self.logger.info(
            "Waiting for new tab/window"
        )

        with self.page.expect_popup() as popup_info:

            trigger_action()

        new_page = popup_info.value

        new_page.wait_for_load_state()

        return new_page
    
    def upload_file(
        self,
        locator,
        file_path
    ):

        self.logger.info(
            f"Uploading file: {file_path}"
        )

        self.page.set_input_files(
            locator,
            file_path
        )