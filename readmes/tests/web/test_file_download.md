# tests/web/test_file_download.py — README

Overview
- Purpose: Validate the download link on a local demo page.

Call mapping:
- `page.goto(...)`, `page.locator(...)`, `get_attribute()` → Playwright API

Behavior summary
- Opens local `download_demo.html`, finds the `#download-link`, asserts it is visible and that its `href` equals `sample_download.txt`.

---
Generated README for `tests/web/test_file_download.py`.