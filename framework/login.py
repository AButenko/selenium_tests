# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait


class wait_for_page_load(object):

    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def wait_for(self, condition_function):
        start_time = time.time()
        while time.time() < start_time + 3:
            if condition_function():
                return True
            else:
                time.sleep(0.1)
        raise Exception(
            'Timeout waiting for {}'.format(condition_function.__name__)
        )

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id

    def __exit__(self, *_):
        self.wait_for(self.page_has_loaded)


def login(driver, username="user@phptravels.com", password="demouser", login_page="http://www.phptravels.net/login"):
    if login_page:
        driver.get(login_page)
        assert "Login" in driver.title
    name = driver.find_element_by_name("username")
    name.send_keys(username)
    psswd = driver.find_element_by_name("password")
    psswd.send_keys(password)
    with wait_for_page_load(driver):
        psswd.send_keys(Keys.RETURN)
    # wait = WebDriverWait(driver, 2)
    # wait.until(EC.title_is("My Account"))
    assert "My Account" in driver.title
    assert "Hi, " in driver.page_source


if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        login(driver)
    finally:
        driver.close()