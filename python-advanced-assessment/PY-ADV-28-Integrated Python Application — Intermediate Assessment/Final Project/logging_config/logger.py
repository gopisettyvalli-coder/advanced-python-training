import logging
import os

from config.settings import LOG_FILE

def get_logger():

    folder = os.path.dirname(LOG_FILE)

    if folder:
        os.makedirs(folder, exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger("EmployeeManagement")