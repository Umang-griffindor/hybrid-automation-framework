import logging  # Python stdlib logging module for consistent framework logging
import os  # Python stdlib os module for path manipulation and directory creation


def get_logger():  # helper function that returns a configured Python logger
    """Return a named logger that always has a file handler writing to logs/framework.log.

    Uses a logger named 'framework' to avoid interfering with other logging configuration.
    Ensures the `logs` directory exists, adds a FileHandler only if one targeting
    `framework.log` isn't already present, and disables propagation so messages
    aren't duplicated by the root logger.
    """

    logs_dir = os.path.join(os.getcwd(), "logs")  # build absolute path for logs directory
    os.makedirs(logs_dir, exist_ok=True)  # create logs directory if it does not exist

    logger = logging.getLogger("framework")  # get or create a named logger for this framework
    logger.setLevel(logging.INFO)  # set log level to INFO for framework diagnostics

    # Add a FileHandler for framework.log if one isn't already present.
    desired_logfile = os.path.join(logs_dir, "framework.log")  # target log file path
    has_file_handler = False  # boolean used to avoid duplicate handlers
    for h in logger.handlers:  # iterate existing handlers to detect duplicates
        base = getattr(h, "baseFilename", None)
        if base and os.path.abspath(base) == os.path.abspath(desired_logfile):
            has_file_handler = True
            break

    if not has_file_handler:  # only add handlers once to avoid repeated logs
        file_handler = logging.FileHandler(desired_logfile)  # file handler writes logs to disk
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )  # log format pattern for consistent output
        file_handler.setFormatter(formatter)  # apply formatter to file handler
        logger.addHandler(file_handler)  # attach file handler to the logger

        console_handler = logging.StreamHandler()  # stream handler prints logs to console

        console_handler.setFormatter(
            formatter
        )  # use same formatter for console output

        logger.addHandler(console_handler)  # attach console handler to logger

    # Prevent messages from being propagated to the root logger (avoids duplicates).
    logger.propagate = False

    return logger  # return the configured logger for use across the framework