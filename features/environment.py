from selenium import webdriver
from selenium.common.exceptions import WebDriverException

SUT_URL = "http://localhost:8080/" # FIXME unused
def get_driver():
    """Get Chrome/Firefox driver from Selenium Hub"""
    try:
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=webdriver.ChromeOptions()
        )
    except WebDriverException:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=webdriver.FirefoxOptions())

    # determines response wait time - set longer if you want to overview the
    # state on which the test got stuck via localhost:7900 (selenium grid)
    # recommended - 1 for casual testing run | 15 for human reviewing [in seconds]
    driver.implicitly_wait(15)
    return driver

def before_all(context):
    """Gets driver at the start of all test run"""
    context.driver = get_driver()
def after_all(context):
    """Releases driver at the end of all test run"""
    context.driver.quit()
