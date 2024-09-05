import json
import yaml
import logging

# ===== READ/WRITE DATA FORMAT =====
def read_yaml(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML: {e}")


# ===== STRING-DICT CONVERSION =====
def json_to_str(payload: dict) -> str:
    return json.dumps(payload)

def str_to_json(payload: str) -> dict:
    try:
        return json.loads(payload)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON string: {e}")


# ===== LOGGING SYSTEM =====
def set_logger(level: int = logging.DEBUG, file_path: str = None) -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    formatter = logging.Formatter('[%(asctime)s] - %(levelname)7s --- %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    if file_path:
        try:
            file_handler = logging.FileHandler(file_path)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error creating log file: {e}")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger  