# -*- coding: utf-8 -*-
import time

from tools import wait_for_page_load, page_contain_assert
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait


def enter_login_credentials(driver, username, password):
    name = driver.find_element_by_name("username")
    name.send_keys(username)
    psswd = driver.find_element_by_name("password")
    psswd.send_keys(password)
    return name, psswd


def login(driver, username="user@phptravels.com", password="demouser", login_page="http://www.phptravels.net/login"):
    if login_page:
        driver.get(login_page)
    page_contain_assert(driver, title=["Login"], page_source=["Email", "Password", "Remember Me",
                                                    "Login", "Sign Up", "Forget Password"])
    name, psswd = enter_login_credentials(driver, username, password)
    with wait_for_page_load(driver):
        psswd.send_keys(Keys.RETURN)
    # wait = WebDriverWait(driver, 2)
    # wait.until(EC.title_is("My Account"))
    page_contain_assert(driver, title=["My Account"], page_source=["Hi, ", "Booking",
                                                                   "My Profile", "Wishlist", "Newsletter"])


def logout(driver, logout_page="http://phptravels.net/account/logout/"):
    if logout_page not in driver.page_source:
        login(driver)
    page_contain_assert(driver, page_source=[logout_page])
    driver.get(logout_page)
    page_contain_assert(driver, title=["Login"])


if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        login(driver)
    finally:
        driver.close()