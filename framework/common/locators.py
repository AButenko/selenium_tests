from enum import Enum

from selenium.webdriver.common.by import By


HOMEPAGE = "http://phptravels.net"


class HeaderLocators(object):

        LOGO = (By.XPATH , "//div[@class='navbar']/div/a")

        class NAV(Enum):
            HOME = (By.XPATH , "//div[@class='navbar']/div/ul/li/a[@href='%s/']" % HOMEPAGE)
            HOTELS = (By.XPATH, "//div[@class='navbar']/div/ul/li/a[@href='%s/hotels']" % HOMEPAGE)
            TOURS = (By.XPATH, "//div[@class='navbar']/div/ul/li/a[@href='%s/tours']" % HOMEPAGE)
            FLIGHTS = (By.XPATH, "//div[@class='navbar']/div/ul/li/a[@href='%s/flightsd']" % HOMEPAGE)
            CARS = (By.XPATH, "//div[@class='navbar']/div/ul/li/a[@href='%s/cars']" % HOMEPAGE)
            OFFERS = (By.XPATH, "//div[@class='navbar']/div/ul/li/a[@href='%s/offers']" % HOMEPAGE)
            BLOG = (By.XPATH, "//div[@class='navbar']/div/ul/li/a[@href='%s/blog']" % HOMEPAGE)
