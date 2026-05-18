from pages.login_page import LoginPage  # import login page object for invalid login validation

def test_invalid_login(page):  # Playwright test that verifies error handling for bad credentials

    login_page = LoginPage(page)  # instantiate the login page object

    login_page.open_login_page()  # navigate to login page using config-driven URL

    login_page.login(
        "wrong_user",
        "wrong_password"
    )  # attempt login with invalid credentials

    assert "Your username is invalid!" in (
        page.locator("#error").text_content()
    )  # assert that the expected error message is displayed