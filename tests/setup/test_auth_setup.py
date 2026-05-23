from pathlib import Path
from pages.login_page import LoginPage


def test_auth_setup(page):

    auth_dir = Path("auth")

    auth_dir.mkdir(
        exist_ok=True
    )

    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.login(
        "student",
        "Password123"
    )

    page.context.storage_state(
        path="auth/auth_state.json"
    )

    print(
        "Authentication state saved"
    )