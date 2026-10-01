from config.settings import logger

def create_employee():
    logger.info("Employee created")

def update_employee():
    logger.info("Employee updated")

def delete_employee():
    logger.info("Employee deleted")


def search_employee():
    logger.info("Employee searched")


def validation_failure():
    logger.warning("Validation failure")


def unexpected_error():
    logger.error("Unexpected error")


logger.info("Application started")

create_employee()
update_employee()
delete_employee()
search_employee()
validation_failure()
unexpected_error()

logger.info("Application stopped")