# pages/login_page.py — README

Overview
- Purpose: Page Object Model for the login page. Wraps page-specific selectors and flows and reuses `BasePage` helpers.
- Dependencies: `pages.base_page.BasePage`, `utils.config_reader.ConfigReader`.

Class: `LoginPage(BasePage)`
- Class-level selector constants:
  - `USERNAME_INPUT = "#username"`
  - `PASSWORD_INPUT = "#password"`
  - `SUBMIT_BUTTON = "#submit"`
  - `SUCCESS_MESSAGE = ".post-title"`

- `__init__(self, page)`
  - Calls `super().__init__(page)` to initialize `self.page` and `self.logger`.
  - Loads `self.config = ConfigReader.read_config()` (reads environment config JSON).

- `open_login_page(self)`
  - Calls `self.navigate(self.config["base_url"])` (BasePage.navigate).

- `login(self, username, password)`
  - Reuses base helpers: `wait_for_element_visible`, `enter_text` for username/password, and `safe_click` to submit.

- `get_success_message(self)`
  - Returns `self.get_element_text(self.SUCCESS_MESSAGE)` (BasePage.get_element_text).

Detailed notes
- `self` refers to the `LoginPage` instance. When `login()` calls `self.enter_text(...)`, it uses the `enter_text` method inherited from `BasePage`.
- `ConfigReader.read_config()` uses environment variable `TEST_ENV` (defaults to `qa`) and reads `configs/<env>_config.json`.

Example usage in tests
```python
login = LoginPage(page)
login.open_login_page()
login.login("user","pass")
msg = login.get_success_message()
```

---
Generated README for `pages/login_page.py`.