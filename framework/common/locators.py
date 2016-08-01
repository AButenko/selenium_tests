from enum import Enum

from selenium.webdriver.common.by import By


HOMEPAGE = "http://phptravels.net"


class HeaderLocators(object):

        LOGO = (By.XPATH , "//div[@class='navbar']/div/a")

        class NAV(Enum):
            HOME        = (By.XPATH , "//div[@class='navbar']/div/ul/li/a[@href='%s/']" % HOMEPAGE)
            HOTELS      = (By.XPATH, "//div[@class='navbar']/div/ul/li/a[@href='%s/hotels']" % HOMEPAGE)
            TOURS       = (By.XPATH, "//div[@class='navbar']/div/ul/li/a[@href='%s/tours']" % HOMEPAGE)
            FLIGHTS     = (By.XPATH, "//div[@class='navbar']/div/ul/li/a[@href='%s/flightsd']" % HOMEPAGE)
            CARS        = (By.XPATH, "//div[@class='navbar']/div/ul/li/a[@href='%s/cars']" % HOMEPAGE)
            OFFERS      = (By.XPATH, "//div[@class='navbar']/div/ul/li/a[@href='%s/offers']" % HOMEPAGE)
            BLOG        = (By.XPATH, "//div[@class='navbar']/div/ul/li/a[@href='%s/blog']" % HOMEPAGE)

        class ACCOUNT(Enum):
            LOGIN       = (By.XPATH, "//div[@class='navbar']/div/ul/li/a[@href='%s/login']" % HOMEPAGE)
            SIGN_UP     = (By.XPATH, "//div[@class='navbar']/div/ul/li/a[@href='%s/register']" % HOMEPAGE)
            ACCOUNT     = (By.XPATH, "//div[@class='navbar']/div/ul/li/ul/li/a[@href='%s/account']" % HOMEPAGE)
            LOGOUT      = (By.XPATH, "//div[@class='navbar']/div/ul/li/ul/li/a[@href='%s/account/logout']" % HOMEPAGE)

        class LANGUAGES(Enum):
            _base       = (By.XPATH, "//div[@class='navbar']/div/ul/li/a/img")
            Arabic      = (By.XPATH, "//div[@class='navbar']/div/ul/li/ul/li/a[@data-langname='Arabic']")
            Filipino    = (By.XPATH, "//div[@class='navbar']/div/ul/li/ul/li/a[@data-langname='Filipino']")
            French      = (By.XPATH, "//div[@class='navbar']/div/ul/li/ul/li/a[@data-langname='French']")
            Russian     = (By.XPATH, "//div[@class='navbar']/div/ul/li/ul/li/a[@data-langname='Russian']")
            Malay       = (By.XPATH, "//div[@class='navbar']/div/ul/li/ul/li/a[@data-langname='Malay']")
            Spanish     = (By.XPATH, "//div[@class='navbar']/div/ul/li/ul/li/a[@data-langname='Spanish']")
            Portuguese  = (By.XPATH, "//div[@class='navbar']/div/ul/li/ul/li/a[@data-langname='Portuguese']")
            English     = (By.XPATH, "//div[@class='navbar']/div/ul/li/ul/li/a[@data-langname='English']")
            Ukrainian   = (By.XPATH, "//div[@class='navbar']/div/ul/li/ul/li/a[@data-langname='Ukrainian']")
            Italian     = (By.XPATH, "//div[@class='navbar']/div/ul/li/ul/li/a[@data-langname='Italian']")

        class CURRENCY(Enum):
            US_DOLLAR   = (By.XPATH, "//div[@class='navbar']/div/ul//select[@id='currency']/option[@value='1']")
            GB_POUND    = (By.XPATH, "//div[@class='navbar']/div/ul//select[@id='currency']/option[@value='3']")
            SR_SAURI    = (By.XPATH, "//div[@class='navbar']/div/ul//select[@id='currency']/option[@value='9']")
            EURO        = (By.XPATH, "//div[@class='navbar']/div/ul//select[@id='currency']/option[@value='10']")
