from loguru import logger

logger.debug("info for the developer")
logger.info("information of the process")
logger.warning("a warning that something will be deprecated in the future")
logger.error("failure")
logger.critical("failure that abort the app")