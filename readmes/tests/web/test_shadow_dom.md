# tests/web/test_shadow_dom.py — README

Overview
- Purpose: Demonstrates accessing shadow DOM elements by chaining `locator()` calls.

Call mapping:
- `page.locator(parent).locator(child)` → Playwright chained locators for shadow DOM

Behavior summary
- Loads a local `shadow_dom_demo.html`, chains locators to reach `#shadow-button` under host `#host`, and asserts visibility.

---
Generated README for `tests/web/test_shadow_dom.py`.