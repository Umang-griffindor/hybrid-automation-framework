# tests/web/test_spinner_wait.py — README

Overview
- Purpose: Validate waiting for a spinner/loader to disappear using `LoginPage.wait_for_spinner_to_disappear`.

Call mapping:
- `LoginPage.open_login_page()` → `pages/login_page.py`
- `LoginPage.wait_for_spinner_to_disappear()` → `pages/login_page.py` → `BasePage.wait_for_spinner_to_disappear()`

Behavior summary
- Opens login page and waits for `.loading-spinner` to become hidden.

---
Generated README for `tests/web/test_spinner_wait.py`.