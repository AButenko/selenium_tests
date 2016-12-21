from contextlib import contextmanager

from selenium.webdriver.support.expected_conditions import staleness_of, visibility_of
from selenium.webdriver.support.wait import WebDriverWait


@contextmanager
def wait_for_page_load(driver, timeout=5):
    """
    Explicitly wait for loading/reloading of the whole web page.
    Args:
        driver:         selenium webdriver instance.
        timeout:        timeout for waiting.

    Returns:

    """
    old_page = driver.find_element_by_tag_name('html')
    yield
    WebDriverWait(driver, timeout).until(
        staleness_of(old_page)
    )

@contextmanager
def wait_for_element_load(driver, old_element, timeout=5):
    """
    Explicitly wait for loading/reloading of element.
    Args:
        driver:         selenium webdriver instance.
        old_element:    element we are waiting to be disappeared/refreshed.
        timeout:        timeout for waiting.

    Returns:

    """
    yield
    WebDriverWait(driver, timeout).until(
        staleness_of(old_element)
    )


@contextmanager
def wait_for_element_visibility(driver, element, timeout=5):
    """
    Explicitly wait while element becomes visible.
    Args:
        driver:         selenium webdriver instance.
        element:        element we are waiting to be visible.
        timeout:        timeout for waiting.

    Returns:

    """
    yield
    WebDriverWait(driver, timeout).until(
        visibility_of(element)
    )


def page_contain_assert(driver, title=[], page_source=[]):
    """
    Assert helper for checking if page or page title contain some text.
    Args:
        driver:         selenium webdriver instance.
        title:          list of strings to check if they are in page title.
        page_source:    list of strings to check if they are in page source.

    Returns:

    """
    for i in title:
        assert i in driver.title
    for i in page_source:
        assert i in driver.page_source
