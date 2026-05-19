# utils/screenshot_utils.py — README

Overview
- Purpose: Utility to produce a timestamped file path for test screenshots.

Function: `generate_screenshot_path(test_name)`
- Builds a timestamp using `datetime.now().strftime("%Y%m%d_%H%M%S")`.
- Ensures `screenshots` directory exists (creates it if not present).
- Returns a path string like `screenshots/<test_name>_YYYYMMDD_HHMMSS.png`.

Notes
- This helper only generates a filesystem path; actual screenshots are taken by Playwright (e.g., `page.screenshot(path=...)`).

Example
```python
path = generate_screenshot_path('test_login')
page.screenshot(path=path)
```

---
Generated README for `utils/screenshot_utils.py`.