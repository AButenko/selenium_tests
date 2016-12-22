from framework.gui.common.header import PageHeader


class BasePage(object):

    def __init__(self, driver):
        self._driver = driver
        self.header = PageHeader(driver)