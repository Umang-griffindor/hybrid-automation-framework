from pages.login_page import LoginPage  # import login page object for waits and visibility checks


def test_wait_example(page):  # Playwright test that demonstrates explicit waiting for elements

    login_page = LoginPage(page)  # instantiate login page object

    login_page.open_login_page()  # navigate to login page before checking elements

    login_page.wait_for_element_visible(
        login_page.USERNAME_INPUT
    )  # wait until the username input is visible before assertions

    assert (
        page.locator(
            login_page.USERNAME_INPUT
        ).is_visible()
    )  # assert the username input is visible using Playwright locator