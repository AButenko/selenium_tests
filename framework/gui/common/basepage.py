from framework.gui.common.header import PageHeader


class BasePage(object):

    def __init__(self, driver, logger=None):
        self.logger = logger
        self._driver = driver
        self.header = PageHeader(driver, logger)