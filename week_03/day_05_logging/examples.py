# Неделя 3, День 5 — Примеры

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

logging.info("Application started")
logging.warning("Config file is missing, using defaults")
logging.error("Failed to load test data")


def divide(a: int, b: int) -> float:
    logging.info("Dividing %s by %s", a, b)
    return a / b


try:
    print(divide(10, 2))
except ZeroDivisionError:
    logging.error("Division by zero")
