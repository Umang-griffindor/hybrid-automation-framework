# utils/config_reader.py — README

Overview
- Purpose: Loads environment-specific JSON config files for tests.
- Behavior: Reads `TEST_ENV` environment variable (defaults to `qa`) then opens `configs/<env>_config.json`.

Class: `ConfigReader`
- `read_config()` (static)
  - Reads `TEST_ENV` env var or defaults to `qa`.
  - Prints the environment being used for clarity when running tests.
  - Loads and returns the parsed JSON config dict.

Notes
- Example config keys expected by tests: `base_url`, `api_base_url`.
- If the file path is incorrect or the JSON is invalid, file IO/JSON exceptions will be raised.

Example
```python
config = ConfigReader.read_config()
print(config['base_url'])
```

---
Generated README for `utils/config_reader.py`.