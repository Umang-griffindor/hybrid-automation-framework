# tests/api/test_api_users.py — README

Overview
- Purpose: API test that creates a post using the framework `APIClient` and validates the response using `ResponseValidator`.
- Dependencies called by this test:
  - `ConfigReader.read_config()` (from `utils.config_reader`) to obtain `api_base_url`.
  - `APIClient.post()` (from `api.api_client`) to send the POST.
  - `APIHeaders.default_headers()` (from `api.api_headers`) to supply headers.
  - `ResponseValidator.validate_status_code()` and `validate_json_key()` (from `api.response_validator`) to assert response correctness.

Call mapping (what this test calls and where defined):
- `ConfigReader.read_config()` → `utils/config_reader.py`
- `APIClient.post()` → `api/api_client.py`
- `APIHeaders.default_headers()` → `api/api_headers.py`
- `ResponseValidator.validate_status_code()` → `api/response_validator.py`
- `ResponseValidator.validate_json_key()` → `api/response_validator.py`

Behavior summary
- Build payload dict, call `api_client.post(f"{config['api_base_url']}/posts", payload=..., headers=...)`.
- Parse JSON, assert status 201 and ensure `title` key in JSON.

---
Generated README for `tests/api/test_api_users.py`.