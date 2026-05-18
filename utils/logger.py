import logging
import os


def get_logger():
    """Return a named logger that always has a file handler writing to logs/framework.log.

    Uses a logger named 'framework' to avoid interfering with other logging configuration.
    Ensures the `logs` directory exists, adds a FileHandler only if one targeting
    `framework.log` isn't already present, and disables propagation so messages
    aren't duplicated by the root logger.
    """

    logs_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_dir, exist_ok=True)

    logger = logging.getLogger("framework")
    logger.setLevel(logging.INFO)

    # Add a FileHandler for framework.log if one isn't already present.
    desired_logfile = os.path.join(logs_dir, "framework.log")
    has_file_handler = False
    for h in logger.handlers:
        base = getattr(h, "baseFilename", None)
        if base and os.path.abspath(base) == os.path.abspath(desired_logfile):
            has_file_handler = True
            break

    if not has_file_handler:
        file_handler = logging.FileHandler(desired_logfile)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(
            formatter
        )

        logger.addHandler(console_handler)

    # Prevent messages from being propagated to the root logger (avoids duplicates).
    logger.propagate = False

    return logger