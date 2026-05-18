from pages.login_page import LoginPage  # import login page object for testing network monitoring


def test_network_response(page):  # Playwright test that validates network response interception

    login_page = LoginPage(page)  # instantiate login page object

    response = login_page.wait_for_response(

        lambda: login_page.open_login_page(),

        "practice-test-login"
    )  # wait for a network response containing the expected URL fragment

    print(
        f"Response Status: "
        f"{response.status}"
    )  # debug print of the network response status code

    print(
        f"Response URL: "
        f"{response.url}"
    )  # debug print of the intercepted response URL

    assert response.status == 200  # assert that the intercepted network response succeeded