import logging

def setup_logger(name, log_file, level=logging.INFO):
    """
    Set up a logger for logging information to a file.
    """
    try:
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        return logger
    except Exception as e:
        print(f"Error setting up logger: {e}")
        return None

def handle_error(error_message):
    """
    General error handler for the application.
    """
    print(f"Error: {error_message}")

