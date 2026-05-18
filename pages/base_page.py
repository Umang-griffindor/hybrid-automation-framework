from playwright.sync_api import expect  # Playwright import for explicit expectation assertions
from utils.logger import get_logger  # import custom logger builder for reusable logging


class BasePage:  # Python base page class with common Playwright page actions

    def __init__(self, page):  # constructor stores the Playwright page object

        self.page = page  # Playwright Page object used across methods
        self.logger = get_logger()  # create logger for tracing Playwright actions


    def navigate(self, url):  # open a URL in the browser using Playwright

        self.logger.info(f"Opening URL: {url}")  # log the navigation request

        self.logger.info(
            f"Navigating to URL: {url}"
        )  # duplicate log to show intent in different log contexts

        self.page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )  # Playwright goto method navigates to the provided URL in the browser

        self.page.wait_for_load_state("networkidle")  # wait until network activity settles after navigation


    def get_title(self):  # retrieve current page title via Playwright

        return self.page.title()  # returns the browser page title string


    def click_element(self, locator):  # click an element located by CSS or selector

        self.logger.info(
            f"Clicking locator: {locator}"
        )  # log the locator targeted for the click action

        self.page.locator(locator).click()  # Playwright click on the located element


    def enter_text(self, locator, text):  # fill text into an input field

        self.logger.info(
            f"Entering text into locator: {locator}"
        )  # log the field being populated

        self.page.locator(locator).fill(text)  # Playwright fill method enters text into the input


    def wait_for_element(self, locator):  # generic wait for visibility helper

        self.page.locator(locator).wait_for(state="visible")  # Playwright wait_for ensures the element becomes visible


    def is_element_visible(self, locator):  # check whether an element is visible

        return self.page.locator(locator).is_visible()  # returns boolean from Playwright locator


    def get_element_text(self, locator):  # retrieve text content from a locator

        self.logger.info(
            f"Getting text from locator: {locator}"
        )  # log the element text retrieval operation

        return self.page.locator(locator).text_content()  # return the visible text from the element


    def expect_element_visible(self, locator):  # explicit assertion helper for visibility

        expect(self.page.locator(locator)).to_be_visible()  # Playwright expect syntax verifies visibility state

    def wait_for_element_visible(
        self,
        locator,
        timeout=30000
        ):

        self.logger.info(
        f"Waiting for element visibility: "
        f"{locator}"
        )  # log the locator and timeout for visibility wait

        self.page.locator(locator).wait_for(
        state="visible",
        timeout=timeout
        )  # wait until the locator becomes visible or timeout triggers
    
    def wait_for_element_hidden(
        self,
        locator,
        timeout=30000
        ):

        self.logger.info(
        f"Waiting for element hidden: "
        f"{locator}"
        )  # log waiting for element to disappear from view

        self.page.locator(locator).wait_for(
        state="hidden",
        timeout=timeout
        )  # Playwright wait_for hidden state keeps tests stable

    def wait_for_text(
        self,
        locator,
        text,
        timeout=30000
        ):

        self.logger.info(
        f"Waiting for text '{text}' "
        f"in locator: {locator}"
        )  # log the expected text and locator

        self.page.locator(locator).wait_for(
        timeout=timeout
        )  # wait for the element to exist before checking text

        assert (
        text in
        self.page.locator(locator).text_content()
        )  # Python assertion verifies the expected text is present

    def wait_for_response(
        self,
        trigger_action,
        url_part,
        timeout=30000
    ):

        self.logger.info(
        f"Waiting for response containing: "
        f"{url_part}"
        )  # log the expected network response URL fragment

        with self.page.expect_response(
        lambda response:
        url_part in response.url,
        timeout=timeout
        ) as response_info:

            trigger_action()  # execute the action that triggers the network request

        return response_info.value  # return the Playwright response object for validation
    
    def wait_for_spinner_to_disappear(
        self,
        spinner_locator,
        timeout=30000
    ):

        self.logger.info(
            f"Waiting for spinner to disappear: "
            f"{spinner_locator}"
        )  # log spinner locator before waiting

        self.page.locator(
            spinner_locator
        ).wait_for(
            state="hidden",
            timeout=timeout
        )  # wait until the loading spinner is hidden before proceeding

    def safe_click(
        self,
        locator,
        timeout=30000
    ):

        self.wait_for_element_visible(
            locator,
            timeout
        )  # reuse wait helper to ensure element is ready

        self.logger.info(
            f"Safely clicking element: "
            f"{locator}"
        )  # log safe click intent

        self.page.locator(locator).click()  # perform the click after wait

    def get_frame_locator(
        self,
        frame_locator
    ):

        self.logger.info(
            f"Switching to iframe: "
            f"{frame_locator}"
        )  # log iframe locator for debugging

        return self.page.frame_locator(
            frame_locator
        )  # return Playwright frame locator for nested interactions
    
    def get_shadow_locator(
        self,
        parent_locator,
        child_locator
    ):

        self.logger.info(
            f"Accessing shadow DOM element: "
            f"{child_locator}"
        )  # log shadow DOM access, helpful when debugging hidden elements

        return self.page.locator(
            parent_locator
        ).locator(
            child_locator
        )  # chain Playwright locators to access shadow DOM children
    
    def wait_for_new_tab(
        self,
        trigger_action
    ):

        self.logger.info(
            "Waiting for new tab/window"
        )  # log tab popup handling

        with self.page.expect_popup() as popup_info:

            trigger_action()  # execute action that opens a new browser tab

        new_page = popup_info.value  # capture the new page object from the popup

        new_page.wait_for_load_state()  # wait for the new tab to finish loading

        return new_page  # return the new Playwright Page instance
    
    def upload_file(
        self,
        locator,
        file_path
    ):

        self.logger.info(
            f"Uploading file: {file_path}"
        )  # log the file upload path and target element

        self.page.set_input_files(
            locator,
            file_path
        )  # Playwright file upload syntax