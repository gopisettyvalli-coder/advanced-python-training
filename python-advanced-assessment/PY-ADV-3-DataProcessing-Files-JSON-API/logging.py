import logging

logging.basicConfig(
    filename="application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")

print("Program is running")

logging.info("Data received successfully")

print("Data processing completed")

logging.info("Program completed")