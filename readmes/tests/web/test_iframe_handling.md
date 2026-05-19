# tests/web/test_iframe_handling.py — README

Overview
- Purpose: Demonstrates interacting with elements inside an iframe using Playwright `frame_locator`.

Call mapping:
- `page.frame_locator()` and `frame.locator()` → Playwright API

Behavior summary
- Opens `https://demoqa.com/frames`, selects `#frame1`, finds `#sampleHeading` inside the frame, and asserts its text contains the expected string.

---
Generated README for `tests/web/test_iframe_handling.py`.