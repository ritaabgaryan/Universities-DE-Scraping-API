import json
import logging
import logging.config


def setup_logging(config_path="log/config/logging.json"):
    with open(config_path) as f:
        config = json.load(f)

    if not config.get("enable", True):
        logging.disable(logging.CRITICAL)
        return

    logging.config.dictConfig(config)


def get_logger(name: str):
    return logging.getLogger(f"project.{name}")
