# utils/logger.py — README

Overview
- Purpose: Centralized logger factory used across the framework to ensure consistent logging to `logs/framework.log` and console.
- Dependencies: Python `logging`, `os`.

Function: `get_logger()`
- Creates `logs` directory if missing.
- Uses a named logger `framework` with `INFO` level.
- Adds a `FileHandler` writing to `logs/framework.log` (only if one is not already present) and a `StreamHandler` for console output.
- Sets a formatter: `"%(asctime)s | %(levelname)s | %(name)s | %(message)s"`.
- Disables propagation to avoid duplicate messages via the root logger.

Notes & best practices
- Calling `get_logger()` repeatedly returns the same configured logger instance (handlers are only added once).
- The function uses `baseFilename` detection to avoid duplicate file handlers.

Example
```python
logger = get_logger()
logger.info("Test started")
```

---
Generated README for `utils/logger.py`.