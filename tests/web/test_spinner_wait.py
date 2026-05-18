from pages.login_page import LoginPage


def test_spinner_handling(page):

    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.wait_for_spinner_to_disappear(
        ".loading-spinner"
    )