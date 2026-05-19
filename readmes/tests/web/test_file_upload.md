# tests/web/test_file_upload.py — README

Overview
- Purpose: Validates file upload flow using a local demo HTML page and `BasePage.upload_file` helper.

Call mapping:
- `BasePage.upload_file()` → `pages/base_page.py`
- `page.goto(...)` and `page.locator(...).input_value()` → Playwright API

Behavior summary
- Opens a local `file_upload_demo.html`, resolves `sample_upload.txt` path, calls `base_page.upload_file("#file-upload", file_path)`, then asserts the control's `input_value()` contains the expected filename.

Notes
- Uses `pathlib.Path` to build robust file paths relative to the repo.

---
Generated README for `tests/web/test_file_upload.py`.