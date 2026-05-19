# api/api_headers.py — README

Overview
- Purpose: Provides standard HTTP headers used by API tests, including an Authorization header assembled from the `AuthAPI` token.
- Dependencies: `api.auth.AuthAPI`.

Class: `APIHeaders`
- `default_headers()` (static)
  - Calls `AuthAPI.get_token()` and returns a dict with `Content-Type: application/json` and `Authorization: Bearer <token>`.

Notes
- `AuthAPI.get_token()` currently returns a dummy token. Replace with real auth flow if needed.

Example
```python
headers = APIHeaders.default_headers()
client.get(url, headers=headers)
```

---
Generated README for `api/api_headers.py`.