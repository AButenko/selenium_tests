# -*- coding: utf-8 -*-
from framework.login import login
from selenium import webdriver
import pytest

def test_default_user():
    driver = webdriver.Chrome()
    try:
        login(driver)
    finally:
        driver.close()