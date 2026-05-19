# tests/web/test_waits_demo.py — README

Overview
- Purpose: Demonstrates explicit waits and visibility checks using the `LoginPage` object and `BasePage` helpers.

Call mapping:
- `LoginPage.open_login_page()` → `pages/login_page.py`
- `LoginPage.wait_for_element_visible()` → `pages/login_page.py` → `BasePage.wait_for_element_visible()`

Behavior summary
- Opens login page, waits for username input to be visible, then asserts visibility using Playwright `page.locator(...).is_visible()`.

---
Generated README for `tests/web/test_waits_demo.py`.