from utils import *
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


use_step_matcher("re")


@given("I type in my credentials")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("http://mys01.fit.vutbr.cz:8084/")
    context.driver.find_element(By.CSS_SELECTOR, ".list-inline-item > .dropdown .fa-caret-down").click()
    context.driver.find_element(By.LINK_TEXT, "Login").click()
    context.driver.find_element(By.LINK_TEXT, "Login").click()
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").send_keys("matejkonopik@gmail.com")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("1234")

@when('I click enter')
def step_impl(context):
    context.driver.find_element(By.ID, "input-password").send_keys(Keys.ENTER)

@then('I will see my email in the manager page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(1)").click()
    context.driver.find_element(By.LINK_TEXT, "Edit your account information").click()
    value = context.driver.find_element(By.ID, "input-email").get_attribute("value")
    assert value == "matejkonopik@gmail.com"

@given("I am at the homepage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("http://mys01.fit.vutbr.cz:8084/")
    context.driver.find_element(By.CSS_SELECTOR, HOME_BTN).click()


@step("I can see product 'iPhone' in the featured section")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("http://mys01.fit.vutbr.cz:8084/")
    context.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(2) h4").click()
    assert context.driver.find_element(By.LINK_TEXT, "iPhone").text == "iPhone"


@when("I add iPhone to the cart")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("http://mys01.fit.vutbr.cz:8084/")
    context.driver.find_element(By.LINK_TEXT, "iPhone").click()
    context.driver.find_element(By.ID, "button-cart").click()


@then("I can see that the 'iPhone' was added to the shopping cart")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("http://mys01.fit.vutbr.cz:8084/")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-inverse").click()
    context.driver.find_element(By.CSS_SELECTOR, ".text-end > a:nth-child(1) > strong").click()
    assert context.driver.find_element(By.LINK_TEXT, "iPhone") 


#assert context.driver.find_element(By.LINK_TEXT, "iPhone").text == "iPhone" # redundant?



###################### S2 #######################x


@given("I can see iPhone in my cart")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("http://mys01.fit.vutbr.cz:8084/en-gb?route=checkout/cart")
    assert context.driver.find_element(By.LINK_TEXT, "iPhone").text == "iPhone" # redundant?


@when("I click Remove iPhone from the cart")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, "#shopping-cart > div > table > tbody > tr > td:nth-child(4) > form > div > button.btn.btn-danger").click()


@then("I can see that the iPhone was removed from the cart")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # check that there's no iphone in the cart
    assert not check_link_exists_by_link_text("iPhone", driver=context.driver)



############################### S3 ########################################


@given("I am at the 'Canon EOS 5D' detail page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("http://mys01.fit.vutbr.cz:8084/")
    #context.driver.find_element(By.LINK_TEXT, "Cameras").click() # go to home page
    context.driver.find_element(By.LINK_TEXT, "Canon EOS 5D").click() # go to canon detail page

@step("I select 'Red' from the available options")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Select(context.driver.find_element(By.ID, "input-option-226"))\
        .select_by_value("15")



@when("I click 'Add to cart'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.ID, "button-cart").click()

@then("I can see the 'Canon EOS 5D' in 'Red' variation in my shopping cart")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("http://mys01.fit.vutbr.cz:8084/")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-inverse").click()
    context.driver.find_element(By.CSS_SELECTOR, ".text-end > a:nth-child(1) > strong").click()
    assert context.driver.find_element(By.LINK_TEXT, "Canon EOS 5D")
    assert context.driver.find_element(By.CSS_SELECTOR, ".text-wrap > small:nth-child(3)").text == "- Select: Red"



################################## S4 ##############################################


@given("I search for 'iMac' in the top search bar")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("http://mys01.fit.vutbr.cz:8084/")
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("iMac")

@when("I click the search button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, ".fa-magnifying-glass").click()

@then("I should see 'iMac' product in the search results")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver.find_element(By.LINK_TEXT, "iMac").text == "iMac"


