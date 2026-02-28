import logging
import os

def get_logger():

    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)

    logger = logging.getLogger("SauceDemoLogger")
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if not logger.handlers:

        file_path = os.path.join(log_folder, "test.log")

        file_handler = logging.FileHandler(file_path, mode="a")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger