# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys

from framework import login, tools
from selenium import webdriver
import pytest


def enter_login_page(driver):
    driver.get("http://www.phptravels.net/login")


def test_login_default_user():
    driver = webdriver.Chrome()
    try:
        login.login(driver)
    finally:
        driver.close()


@pytest.mark.parametrize("user, psswd",[('',''), ('user@phptravels.com', '')])
def test_login_any_user(user, psswd):
    driver = webdriver.Chrome()
    try:
        enter_login_page(driver)
        login.page_contain_assert(driver, title=["Login"], page_source=["Email", "Password", "Remember Me",
                                                        "Login", "Sign Up", "Forget Password"])
        psswd = login.enter_login_credentials(driver, user, psswd)
        # with tools.wait_for_page_load(driver):
        psswd.send_keys(Keys.RETURN)
        #TODO

    finally:
        driver.close()


def test_logout_default_user():
    driver = webdriver.Chrome()
    try:
        login.logout(driver)
    finally:
        driver.close()