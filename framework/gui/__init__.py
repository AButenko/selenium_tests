import os
from logging.config import fileConfig

# This creates selenium.log for last test run to help you in troubleshooting.
fileConfig(os.path.dirname(os.path.abspath(__file__)) + '/selenium_logging.ini')
