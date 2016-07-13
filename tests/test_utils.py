from sumologic.utils import get_logging_level
import logging


def test_logging_level_true():
    level = get_logging_level(True)
    assert logging.DEBUG == level


def test_logging_level_false():
    level = get_logging_level(False)
    assert logging.INFO == level
