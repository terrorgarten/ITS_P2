# import generalization for all features
from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

import random
import string


# generally useful buttons
BASKET_BTN = '.btn-inverse'
HOME_BTN = '#logo .img-fluid'
# admin credentials
ADMIN_USERNAME = "user"
ADMIN_PASSWORD = "bitnami"

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

def get_random_string(length: int) -> str:
    """
    Generates random string of <length> characters
    :param length: String length
    :return string:
    """
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return str(result_str)

def open_my_account_menu(driver: webdriver) -> None:
    """
    Custom function to use some html magic to hack the dropdown of My Account opening, as it can not be opened by selenium click()
    :param driver: The webdriver. pass active context.driver object.
    :return: None
    """
    toggler = driver.find_element(By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul')
    driver.execute_script("arguments[0].setAttribute('class','dropdown-menu dropdown-menu-right show')", toggler)

def turn_off_order_modal(driver: webdriver) -> None:
    modal = driver.find_element(By.ID, "modal-cart")
    driver.execute_script("arguments[0].setAttribute('class', 'modal')", modal)