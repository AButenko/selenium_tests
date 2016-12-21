import contextlib
import pytest
from selenium import webdriver

from framework.gui.common.locators import HOMEPAGE


@pytest.fixture(scope="function")
def browser():
    """
    Pytest fixture, executes in scope of function.
    Creates selenium webdriver instance for interacting with chosen browser and goes to homepage.
    Returns:        selenium webdriver instance.

    """
    driver = webdriver.Chrome()
    with contextlib.closing(driver):
        driver.get(HOMEPAGE)
        yield driver
