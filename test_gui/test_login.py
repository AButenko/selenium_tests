# -*- coding: utf-8 -*-
# from django.conf import settings
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from framework.fixtures import logger
from framework.gui.common.fixtures import browser
from framework.gui.common.tools import page_contain_assert
from framework.gui.loginpage import LoginPage


def test_login_default_user(logger, browser):
    logger.info("Simple login test.")
    loginpage = LoginPage(browser)
    loginpage.login()


@pytest.mark.parametrize("user, psswd",[('',''), ('user@phptravels.com', '')])
def test_login_any_user(logger, browser, user, psswd):
    loginpage = LoginPage(browser)
    browser.get(loginpage.login_page)
    name, passwd = loginpage.enter_login_credentials(user, psswd)
    # with tools.wait_for_page_load(browser):
    passwd.send_keys(Keys.RETURN)
    invalid_input = browser.find_element_by_css_selector("input:invalid")
    assert invalid_input.is_displayed()
    # try:
        # validate_email(user)       # TODO use additional flag to check if email is validS
    if not name:
        assert invalid_input == name
    elif not passwd:
        assert invalid_input == passwd
    # except ValidationError:             # otherwise invalid input if in email field
    # assert not browser.execute_script("return document.getElementById(\"username\").validity.valid")  # javascript way to check the same

    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='resultlogin']/div[1]"))
    )
    assert browser.find_element_by_xpath("//div[@class='resultlogin']/div[1]").text == "Invalid Email or Password"


def test_logout_default_user(logger, browser):
    loginpage = LoginPage(browser)
    loginpage.logout()