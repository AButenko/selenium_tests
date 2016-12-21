import contextlib
import logging
import pytest
from selenium import webdriver

from framework.gui.common.basepage import BasePage
from framework.gui.common.tools import wait_for_page_load

@pytest.fixture(scope='module')
def crt_logger():
    logger = logging.Logger('1'+'.log', level=logging.INFO)
    return logger

@pytest.fixture(scope="function")
def chrome_driver():
    driver = webdriver.Chrome()
    with contextlib.closing(driver):
        yield driver


@pytest.mark.parametrize("header_el",['logo', 'hotels', 'tours', 'flights', "cars", "offers", "blog"])
def test_base(crt_logger, chrome_driver, header_el):
    chrome_driver.get('http://phptravels.net/')
    basepage = BasePage(chrome_driver, crt_logger)
    with wait_for_page_load(chrome_driver):
        getattr(basepage.header, header_el).click()


@pytest.mark.parametrize("language_el",['Arabic', 'Filipino'])
def test_languages(crt_logger, chrome_driver, language_el):
    chrome_driver.get('http://phptravels.net/')
    basepage = BasePage(chrome_driver, crt_logger)
    with wait_for_page_load(chrome_driver):
        lang_el = getattr(basepage.header.languages, language_el.lower())
        lang_el.click()