import functools

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from framework.gui.common.tools import wait_for_element_visibility
from framework.gui.common.locators import HeaderLocators


class ElementGroup(object):

    def __init__(self, driver):
        self._driver = driver

    def __getattribute__(self, item):
        if not callable(super().__getattribute__(item)) and item != "_base" and hasattr(self, "_base"):
            item = super().__getattribute__(item)
            click = functools.partial(self.implicit_click, item=item)
            setattr(item, 'click', click)
            return item
        else:
            return super().__getattribute__(item)

    def implicit_click(self, item):
        actions = ActionChains(self._driver)
        with wait_for_element_visibility(self._driver, item):
            actions.move_to_element(self._base).click().perform()

        # It is needed to clean ActionChains instance after each call of preform()
        actions = ActionChains(self._driver)
        actions.move_to_element(item).click().perform()


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
