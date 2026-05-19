# conftest.py — README

Overview
- Purpose: Pytest hooks and fixtures that run for the test suite. Provides automatic screenshot capture on failures and a test report hook.
- Dependencies: `os`, `pytest`.

Main items
- `pytest_runtest_makereport(item, call)`
  - A `hookwrapper` that yields to let pytest run the test, then attaches the generated report (`rep`) to the test `item` object as attributes like `rep_call`.

- `screenshot_on_failure(request, page)` (fixture, `autouse=True`)
  - Runs around each test function. After the test yields, it checks `request.node.rep_call.failed` and if so, ensures `screenshots` dir exists, calls `page.screenshot(path=...)`, and prints the saved path.
  - `page` is expected to be a Playwright `Page` fixture provided by the test environment.

Commented example
- There's a commented fixture showing how to create and yield a `page` if you want to manage that locally.

Notes
- `autouse=True` means `screenshot_on_failure` runs for every test automatically.
- If Playwright's fixture name differs in your environment, you may need to adapt the fixture signature.

---
Generated README for `conftest.py`.