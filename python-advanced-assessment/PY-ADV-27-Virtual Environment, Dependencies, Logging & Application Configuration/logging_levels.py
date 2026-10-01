import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING message")
logging.error("This is an ERROR message")
logging.critical("This is a CRITICAL message")