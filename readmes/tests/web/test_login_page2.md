# tests/web/test_login_page2.py — README

Overview
- Purpose: Simple UI test verifying invalid login behavior.

Call mapping:
- `LoginPage.open_login_page()` → `pages/login_page.py`
- `LoginPage.login()` → `pages/login_page.py`
- `page.locator("#error").text_content()` → Playwright API

Behavior summary
- Opens the login page, attempts login with bad credentials, asserts the expected error message appears.

---
Generated README for `tests/web/test_login_page2.py`.