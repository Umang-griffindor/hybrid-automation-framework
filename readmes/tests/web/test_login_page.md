# tests/web/test_login_page.py — README

Overview
- Purpose: Data-driven UI test that verifies login success and failure scenarios using `LoginPage` page object.
- Dependencies called:
  - `DataReader.read_json_data()` → `utils/data_reader.py` (loads `test_data/login_test_data.json`).
  - `LoginPage` methods → `pages/login_page.py` which in turn uses `BasePage` helpers from `pages/base_page.py`.

Call mapping (direct calls in this test):
- `DataReader.read_json_data()` → `utils/data_reader.py`
- `LoginPage(page)` instantiation → `pages/login_page.py`
- `login_page.open_login_page()` → `pages/login_page.py` (uses `BasePage.navigate`)
- `login_page.login(...)` → `pages/login_page.py` (uses `BasePage.enter_text`, `BasePage.safe_click`, etc.)
- `login_page.get_success_message()` → `pages/login_page.py` (calls `BasePage.get_element_text`)
- Direct `page.locator(...).text_content()` → Playwright API

Behavior summary
- Parameterized over JSON test data. For each dataset, opens the login page, attempts login, and asserts success message or error message accordingly.

---
Generated README for `tests/web/test_login_page.py`.