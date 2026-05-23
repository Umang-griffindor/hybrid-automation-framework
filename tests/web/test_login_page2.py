def test_login_success(login_page):

    login_page.login(
        "student",
        "Password123"
    )

    assert (
        "Logged In Successfully"
        in login_page.get_success_message()
    )