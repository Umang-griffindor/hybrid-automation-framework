# api/api_client.py — README

Overview
- Purpose: Lightweight wrapper around `requests` to centralize API call logging and reuse.
- Dependencies: `requests`, `utils.logger.get_logger()`.

Class: `APIClient`
- `__init__(self)`
  - Creates `self.logger` via `get_logger()`.

- `get(self, url, headers=None)`
  - Logs the outgoing GET, calls `requests.get(url, headers=headers)`, logs `response.status_code`, returns the `requests.Response` object.

- `post(self, url, payload=None, headers=None)`
  - Logs, calls `requests.post(url, json=payload, headers=headers)`, logs status code, returns the `Response`.

Notes
- Returned object is `requests.Response` (not Playwright). Tests call `.json()` or check `.status_code`.
- Errors from `requests` (connection errors) will propagate unless tests catch them.

Example
```python
client = APIClient()
resp = client.post("https://api.example.com/items", payload={"name":"x"}, headers={})
assert resp.status_code == 201
```

---
Generated README for `api/api_client.py`.