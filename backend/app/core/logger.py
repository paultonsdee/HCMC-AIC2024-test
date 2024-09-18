import logging 

# ===== LOGGING SYSTEM =====
def set_logger(level: int = logging.DEBUG, file_path: str = 'app.log') -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    formatter = logging.Formatter('[%(asctime)s] - %(levelname)7s --- %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    if file_path:
        file_handler = logging.FileHandler(file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger  