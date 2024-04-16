from loguru import logger

#logger.add("my_log_file.log")

# to choose the level of logs to be saved in the log file
logger.add("my_log_file.log", level="CRITICAL")

def sum(x, y):
    try:
        sum = x + y
        logger.info(f"Input of correct values. {sum}")
        return sum
    except:
        logger.critical("You need to input correct values.")

sum(2, "3")