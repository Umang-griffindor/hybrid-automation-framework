# api/response_validator.py — README

Overview
- Purpose: Small helper class with static assertion helpers for API responses.

Class: `ResponseValidator`
- `validate_status_code(response, expected_status)`
  - Static method. Uses `assert response.status_code == expected_status` and raises `AssertionError` with helpful message on mismatch.

- `validate_json_key(response_data, key)`
  - Static method. Asserts `key in response_data` and raises `AssertionError` with message if missing.

Notes
- These are simple assertion helpers intended to make test code clearer and reusable.

Example
```python
ResponseValidator.validate_status_code(resp, 200)
ResponseValidator.validate_json_key(resp.json(), "id")
```

---
Generated README for `api/response_validator.py`.