# tests/api/test_create_user.py — README

Overview
- Purpose: Demonstrates POST to a public API and validates the created resource.

Call mapping (methods and origin files):
- `APIClient.post()` → `api/api_client.py`
- `APIHeaders.default_headers()` → `api/api_headers.py`
- `ResponseValidator.validate_status_code()` → `api/response_validator.py`
- `ResponseValidator.validate_json_key()` → `api/response_validator.py`

Behavior summary
- Sends POST to `https://jsonplaceholder.typicode.com/posts` with a payload, validates the response code is 201, and checks the `title` key exists.

---
Generated README for `tests/api/test_create_user.py`.