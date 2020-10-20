from loguru import logger

from Egida import settings


def setup_settings():
    logger.add(sink=settings.LOG_DIR + "log.txt", rotation="friday at 22:00", compression="zip")
