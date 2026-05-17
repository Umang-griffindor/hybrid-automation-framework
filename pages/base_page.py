from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):

        self.page = page


    def navigate(self, url):

        self.page.goto(url)


    def get_title(self):

        return self.page.title()


    def click_element(self, locator):

        self.page.locator(locator).click()


    def enter_text(self, locator, text):

        self.page.locator(locator).fill(text)


    def wait_for_element(self, locator):

        self.page.locator(locator).wait_for(state="visible")


    def is_element_visible(self, locator):

        return self.page.locator(locator).is_visible()


    def get_element_text(self, locator):

        return self.page.locator(locator).inner_text()


    def expect_element_visible(self, locator):

        expect(self.page.locator(locator)).to_be_visible()