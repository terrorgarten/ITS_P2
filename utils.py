from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By

# generally useful buttons
BASKET_BTN = '.btn-inverse'
HOME_BTN = '#logo .img-fluid'

# procedures for checking elements/links
def check_exists_by_xpath(xpath: str, driver: webdriver) -> bool:
    """
    Checks if an element exists on the current page using xpath expression.
    :param xpath: element xpath to check
    :param driver: behave driver - pass as context.driver
    :return: true if exists, false otherwise
    """
    try:
        driver.find_element_by_xpath(xpath)
        print("utils: element by xpath FOUND")
    except NoSuchElementException:
        print("utils: element by xpath NOT FOUND")
        return False
    return True

def check_link_exists_by_link_text(link_text: str, driver: webdriver) -> bool:
    """
    Checks if an element exists on the current page link text matching.
    :param link_text: element link text to check
    :param driver: behave driver - pass as context.driver
    :return: true if exists, false otherwise
    """
    try:
        driver.driver.find_element(By.LINK_TEXT, link_text)
        print("utils: link by text FOUND")
    except BaseException: #FIXME - add more precise error handling
        print("utils: link by text NOT FOUND")
        return False
    return True