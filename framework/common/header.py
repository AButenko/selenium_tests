
from locators import HeaderLocators


class PageHeader(object):

    def __init__(self, driver):
        self._driver = driver
        self.logo = self._driver.find_element(*HeaderLocators.LOGO)
        for el in list(HeaderLocators.NAV):
            setattr(self, el.name.lower(), self._driver.find_element(*el.value))