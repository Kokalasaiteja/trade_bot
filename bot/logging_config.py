import logging
import os


def setup_logger():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger("trading_bot")

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler("logs/trading_bot.log")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
