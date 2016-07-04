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
        name, psswd = login.enter_login_credentials(driver, user, psswd)
        # with tools.wait_for_page_load(driver):
        psswd.send_keys(Keys.RETURN)
        invalid_input = driver.find_element_by_css_selector("input:invalid")
        assert invalid_input.is_displayed()
        if True: #TODO use regexp here to check if email is valid
            assert invalid_input == name
        else: # otherwise inwalid input if in password field
            assert invalid_input == psswd
        # assert not driver.execute_script("return document.getElementById(\"username\").validity.valid")  # javascript way to check the same
        #TODO check error response from server
    finally:
        driver.close()


def test_logout_default_user():
    driver = webdriver.Chrome()
    try:
        login.logout(driver)
    finally:
        driver.close()