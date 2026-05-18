from pages.login_page import LoginPage  # import page object that includes spinner wait helper


def test_spinner_handling(page):  # pytest test function that waits for a loading spinner to disappear

    login_page = LoginPage(page)  # instantiate the login page object with a Playwright page

    login_page.open_login_page()  # navigate to the login page URL using the page object

    login_page.wait_for_spinner_to_disappear(
        ".loading-spinner"
    )  # wait until the Playwright locator for the spinner becomes hidden