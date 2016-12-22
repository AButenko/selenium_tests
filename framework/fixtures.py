import pytest
from framework.logger import init_logger


@pytest.fixture()
def logger(request, capsys):
    """
    Pytest fixture, executes in scope of module.
    Creates logging file for this module.
    Returns: logging.Logger instance.

    """
    framework_logger = init_logger('../logs/', request.module.__name__ + '__'+ request.node.name)
    framework_logger.info("-------------------------------------------------------------------------------------------")
    framework_logger.info("Started test `{}` from module `{}`".format(request.node.name, request.module.__name__))
    framework_logger.info("-------------------------------------------------------------------------------------------")
    yield framework_logger
    framework_logger.info("-------------------------------------------------------------------------------------------")
    framework_logger.info("Ended test `{}` from module `{}`".format(request.node.name, request.module.__name__))
    framework_logger.info("-------------------------------------------------------------------------------------------")