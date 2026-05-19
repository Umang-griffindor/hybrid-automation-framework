# pages/base_page.py — README

Overview
- Purpose: Provides `BasePage`, a Playwright-based helper class with common browser/page interactions used across UI tests (navigation, clicks, waits, frame/shadow access, uploads, response waiting).
- Dependencies: Playwright Sync API (`expect`) and the framework `logger` from `utils.logger`.

Concepts used (brief)
- `self`: instance reference inside class methods. `self.attr` stores attributes on that specific object.
- `Page`: Playwright tab/session object. Methods include `goto`, `locator`, `frame_locator`, `expect_response`, `expect_popup`, `set_input_files`, `wait_for_load_state`.
- `Locator`: returned by `page.locator(selector)`. Methods: `click()`, `fill()`, `text_content()`, `wait_for(state=...)`, `is_visible()`, `locator(child)` (chaining into shadow DOM).
- `expect(locator)`: Playwright assertion helper (e.g., `.to_be_visible()`).
- Timeouts are in milliseconds (ms).

Class: `BasePage`
- `__init__(self, page)`
  - Stores `self.page` (the Playwright `Page` instance) and `self.logger` (from `get_logger()`). Use: all methods access the same browser tab and logging instance.

Methods (what they do, params, returns, behavior)
- `navigate(self, url)`
  - Params: `url` (str)
  - Logs navigation; calls `page.goto(url, wait_until="domcontentloaded", timeout=60000)` then `page.wait_for_load_state("networkidle")` to reduce flakiness on JS-heavy pages.
  - Raises Playwright `TimeoutError` on slow navigation.

- `get_title(self)`
  - Returns: `page.title()` (string)

- `click_element(self, locator)`
  - Params: `locator` (selector string)
  - Logs then `page.locator(locator).click()`.
  - Note: may be flaky if element not ready; prefer `safe_click`.

- `enter_text(self, locator, text)`
  - Params: `locator`, `text` (str)
  - Uses `page.locator(locator).fill(text)` to clear and type.

- `wait_for_element(self, locator)`
  - Waits until `page.locator(locator).wait_for(state="visible")`.

- `is_element_visible(self, locator)`
  - Returns boolean `page.locator(locator).is_visible()`.

- `get_element_text(self, locator)`
  - Logs and returns `page.locator(locator).text_content()` (may be `None`).

- `expect_element_visible(self, locator)`
  - Uses `expect(self.page.locator(locator)).to_be_visible()` to raise readable test failures.

- `wait_for_element_visible(self, locator, timeout=30000)`
  - Explicit wait for `visible` state with configurable timeout (ms).

- `wait_for_element_hidden(self, locator, timeout=30000)`
  - Waits for `hidden` state (useful for spinners or overlays).

- `wait_for_text(self, locator, text, timeout=30000)`
  - Waits for element to exist, then runs `assert text in locator.text_content()`.
  - Suggestion: prefer `expect(locator).to_contain_text(text, timeout=...)` for clearer failures and retry behavior.

- `wait_for_response(self, trigger_action, url_part, timeout=30000)`
  - Params: `trigger_action` (callable), `url_part` (str)
  - Uses `with page.expect_response(lambda r: url_part in r.url, timeout=timeout) as response_info:` then calls `trigger_action()` inside the context. Returns Playwright `Response` object (`response_info.value`).

- `wait_for_spinner_to_disappear(self, spinner_locator, timeout=30000)`
  - Waits until spinner locator becomes hidden.

- `safe_click(self, locator, timeout=30000)`
  - Calls `wait_for_element_visible` then clicks. Use to reduce flaky clicks.

- `get_frame_locator(self, frame_locator)`
  - Returns `page.frame_locator(frame_locator)` for iframe interactions.

- `get_shadow_locator(self, parent_locator, child_locator)`
  - Returns `page.locator(parent_locator).locator(child_locator)` for shadow DOM.

- `wait_for_new_tab(self, trigger_action)`
  - Uses `with page.expect_popup() as popup_info:` then calls `trigger_action()`; returns the new `Page` instance after `wait_for_load_state()`.

- `upload_file(self, locator, file_path)`
  - Calls `page.set_input_files(locator, file_path)`. `file_path` may be a string or list of strings.

Best practices & notes
- Replace raw `assert` in `wait_for_text` with Playwright `expect` for clearer failures.
- Keep timeouts configurable (constants) if you need to tune across the suite.
- Prefer `safe_click` for UI interactions to reduce flakiness.

Examples
```python
base = BasePage(page)
base.navigate("https://example.com")
base.enter_text("input[name=\'q\']", "query")
base.safe_click("button[type='submit']")
```

---
Generated README for `pages/base_page.py`.