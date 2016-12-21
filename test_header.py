import pytest

from framework.fixtures import crt_logger
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
def test_base(crt_logger, browser, header_el):
    basepage = BasePage(browser, crt_logger)
    with wait_for_page_load(browser):
        getattr(basepage.header, header_el).click()


@pytest.mark.parametrize("language_el",['Arabic', 'Filipino'])
def test_languages(crt_logger, browser, language_el):
    basepage = BasePage(browser, crt_logger)
    with wait_for_page_load(browser):
        lang_el = getattr(basepage.header.languages, language_el.lower())
        lang_el.click()