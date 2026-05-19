# tests/web/test_multi_tab.py — README

Overview
- Purpose: Demonstrate handling a new browser tab using `BasePage.wait_for_new_tab`.

Call mapping:
- `BasePage.wait_for_new_tab()` → `pages/base_page.py`
- Inside `trigger_action`: `page.locator("text=Click Here").click()` → Playwright API

Behavior summary
- Navigates to a page that opens a new window when clicking "Click Here", waits for the popup and returns the new `Page` for assertions.

---
Generated README for `tests/web/test_multi_tab.py`.