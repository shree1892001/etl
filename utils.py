import json
import logging

def setup_logging(log_level, log_path):
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_path), logging.StreamHandler()]
    )
    return logging.getLogger()

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)
