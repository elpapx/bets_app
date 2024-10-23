import logging
import os

def setup_logger(name:str, log_file:str, level=logging.INFO) -> logging.Logger:
    if not os.path.exists('logs'):
        os.mkdir('logs')

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger