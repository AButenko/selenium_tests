import pytest

from framework.fixtures import logger
from framework.gui.common.basepage import BasePage
from framework.gui.common.fixtures import browser
from framework.gui.common.tools import wait_for_page_load


@pytest.mark.parametrize("header_el",[
    'logo',
    'hotels',
    # 'tours',
    'flights',
    # "cars",
    "offers",
    "blog"])
def test_base(logger, browser, header_el):
    basepage = BasePage(browser)
    with wait_for_page_load(browser):
        getattr(basepage.header, header_el).click()


@pytest.mark.parametrize("language_el",['Arabic', 'Filipino', 'Ukrainian'])
def test_languages(logger, browser, language_el):
    basepage = BasePage(browser)
    with wait_for_page_load(browser):
        lang_el = getattr(basepage.header.languages, language_el.lower())
        lang_el.click()