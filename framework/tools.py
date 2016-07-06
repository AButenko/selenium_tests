import time
from contextlib import contextmanager

from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait

PAGE_LOADING_TIMEOUT = 5

class wait_for_page_load(object):

    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def wait_for(self, condition_function):
        start_time = time.time()
        while time.time() < start_time + PAGE_LOADING_TIMEOUT:
            if condition_function():
                return True
            else:
                time.sleep(0.1)
        raise Exception(
            'Timeout waiting for {}'.format(condition_function.__name__)
        )

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id

    def __exit__(self, *_):
        self.wait_for(self.page_has_loaded)


@contextmanager
def wait_for_element_load(driver, old_page, timeout=5):
    '''
    :param driver: selenium webdriver instance
    :param old_page: func for finding old element
    :param timeout: timeout for waiting
    :return:
    '''
    # old_page = self.browser.find_element_by_tag_name('html')
    yield
    WebDriverWait(driver, timeout).until(
        staleness_of(old_page)
    )

def page_contain_assert(driver, title=[], page_source=[]):
    for i in title:
        assert i in driver.title
    for i in page_source:
        assert i in driver.page_source