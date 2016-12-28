# -*- coding: utf-8 -*-
from framework.gui.common.basepage import BasePage
from framework.gui.common.locators import HOMEPAGE
from framework.gui.common.tools import wait_for_page_load, page_contain_assert

from selenium.webdriver.common.keys import Keys


# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = HOMEPAGE + "/login"
        self.logout_page = HOMEPAGE + "/account/logout"

    def enter_login_credentials(self, username, password):
        name = self._driver.find_element_by_name("username")
        name.send_keys(username)
        psswd = self._driver.find_element_by_name("password")
        psswd.send_keys(password)
        return name, psswd

    def login(self, username="user@phptravels.com", password="demouser"):
        self._driver.get(self.login_page)
        page_contain_assert(self._driver, title=["Login"], page_source=["Email", "Password", "Remember Me",
                                                        "Login", "Sign Up", "Forget Password"])
        name, psswd = self.enter_login_credentials(username, password)
        with wait_for_page_load(self._driver):
            psswd.send_keys(Keys.RETURN)
        # wait = WebDriverWait(driver, 2)
        # wait.until(EC.title_is("My Account"))
        page_contain_assert(self._driver, title=["My Account"], page_source=["Hi, ", "Booking",
                                                                             "My Profile", "Wishlist", "Newsletter"])

    def logout(self):
        if self.logout_page not in self._driver.page_source:
            # TODO raise error here
            self.login()
        page_contain_assert(self._driver, page_source=[self.logout_page])
        self._driver.get(self.logout_page)
        page_contain_assert(self._driver, title=["Login"])