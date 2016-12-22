# -*- coding: utf-8 -*-
# from django.conf import settings
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from framework.fixtures import logger

from framework.gui import login

def enter_login_page(driver):
    driver.get("http://www.phptravels.net/login")


def test_login_default_user():
    driver = webdriver.Chrome()
    try:
        login.login(driver)
    finally:
        driver.close()


@pytest.mark.parametrize("user, psswd",[('',''), ('user@phptravels.com', '')])
def test_login_any_user(logger, user, psswd):
    driver = webdriver.Chrome()
    try:
        enter_login_page(driver)
        login.page_contain_assert(driver, title=["Login"], page_source=["Email", "Password", "Remember Me",
                                                        "Login", "Sign Up", "Forget Password"])
        name, passwd = login.enter_login_credentials(driver, user, psswd)
        # with tools.wait_for_page_load(driver):
        passwd.send_keys(Keys.RETURN)
        invalid_input = driver.find_element_by_css_selector("input:invalid")
        assert invalid_input.is_displayed()
        # try:
            # validate_email(user)       # TODO use additional flag to check if email is validS
        if not name:
            assert invalid_input == name
        elif not passwd:
            assert invalid_input == passwd
        # except ValidationError:             # otherwise invalid input if in email field
        # assert not driver.execute_script("return document.getElementById(\"username\").validity.valid")  # javascript way to check the same

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='resultlogin']/div[1]"))
        )
        assert driver.find_element_by_xpath("//div[@class='resultlogin']/div[1]").text == "Invalid Email or Password"

    finally:
        driver.close()


def test_logout_default_user(logger):
    driver = webdriver.Chrome()
    try:
        login.logout(driver)
    finally:
        driver.close()