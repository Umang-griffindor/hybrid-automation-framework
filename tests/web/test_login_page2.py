from pages.login_page import LoginPage

def test_invalid_login(browser_page):

    login_page = LoginPage(browser_page)

    login_page.open_login_page()

    login_page.login(
        "wrong_user",
        "wrong_password"
    )

    assert "Your username is invalid!" in (
        browser_page.locator("#error").text_content()
    )