# tests/web/test_flaky.py — README

Overview
- Purpose: Example test demonstrating nondeterministic/flaky behavior by using `random.choice`.

Call mapping:
- `random.choice()` → Python stdlib `random`

Behavior summary
- Test asserts a random boolean; intentionally flaky.

Notes
- Use deterministic mocks or seed `random` for reproducible tests.

---
Generated README for `tests/web/test_flaky.py`.