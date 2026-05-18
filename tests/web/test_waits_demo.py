from pages.login_page import LoginPage


def test_wait_example(page):

    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.wait_for_element_visible(
        login_page.USERNAME_INPUT
    )

    assert (
        page.locator(
            login_page.USERNAME_INPUT
        ).is_visible()
    )