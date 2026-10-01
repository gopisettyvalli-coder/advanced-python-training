import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("This is a debug message")
logging.info("Application started")
logging.warning("This is a warning")
logging.error("An error occurred")
logging.critical("Critical problem occurred")