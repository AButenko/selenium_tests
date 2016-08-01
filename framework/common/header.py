from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from framework.common.tools import wait_for_page_load, wait_for_element_visibility
from locators import HeaderLocators


class ElementGroup(object):

    def __init__(self, driver):
        self._driver = driver

    def __getattribute__(self, item):
        if hasattr(self, "_base"):
            item = object.__getattribute__(self, item)
            def click():
                actions = ActionChains(self._driver)
                with wait_for_element_visibility(self._driver, item):
                    actions.move_to_element(self._base).perform()
                with wait_for_page_load(self._driver):
                    actions.move_to_element(item).click().perform()
            setattr(item, 'click', click)
            return item
        else:
            return object.__getattribute__(self, item)


def set_els_from_locators(cls, locators_list, driver):
    for el in locators_list:
        setattr(cls, el.name.lower(), driver.find_element(*el.value))


class PageHeader(object):

    def __init__(self, driver):
        self._driver = driver
        self.logo = self._driver.find_element(*HeaderLocators.LOGO)
        set_els_from_locators(self, list(HeaderLocators.NAV), self._driver)
        self.account = ElementGroup(self._driver)
        for el in list(HeaderLocators.ACCOUNT):
            try:
                setattr(self.account, el.name.lower(), self._driver.find_element(*el.value))
            except NoSuchElementException as e:
                pass
        self.languages = ElementGroup(self._driver)
        set_els_from_locators(self.languages, list(HeaderLocators.LANGUAGES), self._driver)
        self.currency = ElementGroup(self._driver)
        set_els_from_locators(self.currency, list(HeaderLocators.CURRENCY), self._driver)
