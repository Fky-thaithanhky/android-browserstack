from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720

driver = webdriver.Remote("http://hub.browserstack.com/wd/hub")


# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
