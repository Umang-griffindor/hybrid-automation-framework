# tests/web/test_network_monitoring.py — README

Overview
- Purpose: Validate intercepting/waiting for network responses triggered by UI actions using `LoginPage.wait_for_response`.

Call mapping:
- `LoginPage.wait_for_response()` → `pages/login_page.py` (which uses `BasePage.wait_for_response`)
- `LoginPage.open_login_page()` → `pages/login_page.py`

Behavior summary
- Calls `login_page.wait_for_response(lambda: login_page.open_login_page(), "practice-test-login")`, prints response status and URL, and asserts `response.status == 200`.

Note
- `wait_for_response` requires that the `trigger_action` initiates the request while inside the `expect_response` context.

---
Generated README for `tests/web/test_network_monitoring.py`.