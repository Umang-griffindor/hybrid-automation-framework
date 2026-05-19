# utils/data_reader.py — README

Overview
- Purpose: Helpers for reading test data files (JSON) used by parametrized tests.

Class: `DataReader`
- `read_json_data(file_path)` (static)
  - Opens `file_path`, parses JSON via `json.load()` and returns the resulting Python object (list/dict).

Notes
- `file_path` may be relative to repo root. Tests call `DataReader.read_json_data("test_data/login_test_data.json")`.

Example
```python
test_data = DataReader.read_json_data("test_data/login_test_data.json")
```

---
Generated README for `utils/data_reader.py`.