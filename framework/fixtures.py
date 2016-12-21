import logging
import pytest


@pytest.fixture(scope='module')
def crt_logger():
    """
    Pytest fixture, executes in scope of module.
    Creates logging file for this module.
    Returns: logging.Logger instance.

    """
    logger = logging.Logger('1'+'.log', level=logging.INFO)
    return logger
