import logging


def get_logging_level(debug):
    """Returns logging level based on boolean"""
    level = logging.INFO
    if debug:
        level = logging.DEBUG
    return level
