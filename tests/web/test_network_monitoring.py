from pages.login_page import LoginPage


def test_network_response(page):

    login_page = LoginPage(page)

    response = login_page.wait_for_response(

        lambda: login_page.open_login_page(),

        "practice-test-login"
    )

    print(
        f"Response Status: "
        f"{response.status}"
    )

    print(
        f"Response URL: "
        f"{response.url}"
    )

    assert response.status == 200