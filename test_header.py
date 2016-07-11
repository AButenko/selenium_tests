import pytest

from framework.common.basepage import BasePage
from framework.common.tools import wait_for_page_load
from selenium import webdriver


@pytest.mark.parametrize("header_el",['logo', 'hotels', 'tours', "flights", "cars", "offers", "blog"])
def test_base(header_el):
    driver = webdriver.Chrome()
    try:
        driver.get('http://phptravels.net/')
        basepage = BasePage(driver)
        with wait_for_page_load(driver):
            getattr(basepage.header, header_el).click()
    finally:
        driver.close()