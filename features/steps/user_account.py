from behave import *
from utils import *

use_step_matcher("re")

new_email = ""

@given("I am at the register account page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("http://mys01.fit.vutbr.cz:8084/")
    open_my_account_menu(context.driver)
    context.driver.find_element(By.LINK_TEXT, "Register").click()

@step("I filled in name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("TESTING")

@step("I filled in surname")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.ID, "input-lastname").send_keys("TESTING")


@step("I filled in email in a valid format")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global new_email
    new_email = get_random_string(10)
    context.driver.find_element(By.ID, "input-email").send_keys(new_email + "@test.cz")

@step("I filled in valid password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.ID, "input-password").send_keys("TESTING")


@step("I agreed to the Privacy Policy")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.NAME, "agree").click()

@when("I press the register button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, "#form-register > div > div > button").click()
@then("my account should be created in the system")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver.find_element(By.LINK_TEXT, "Continue").text == "Continue"


#######################################################


@given("I am logged in as user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("http://mys01.fit.vutbr.cz:8084/")
    open_my_account_menu(context.driver)
    assert context.driver.find_element(By.LINK_TEXT, "My Account")

@when("I click the logout button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    open_my_account_menu(context.driver)
    context.driver.find_element(By.LINK_TEXT, "Logout").click()


@then("I will be logged out")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    open_my_account_menu(context.driver)
    assert context.driver.find_element(By.LINK_TEXT, "Login")

#######################################################x

@when("I enter the injection query")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("http://mys01.fit.vutbr.cz:8084/en-gb?route=account/login?id=-1;%27DROP%20ALL%20TABLES--")

@then("I should get an error page or nothing should happen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver.find_element(By.CSS_SELECTOR, "#content > h1").text == "The page you requested cannot be found!"


###########################################################

@step("I filled the form with valid data")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.ID, "input-firstname").send_keys("TESTING")
    context.driver.find_element(By.ID, "input-lastname").send_keys("TESTING")
    context.driver.find_element(By.ID, "input-password").send_keys("TESTING")


@step("I fill in existing account email")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global new_email
    if new_email == "":
        new_email = get_random_string(10)
    context.driver.find_element(By.ID, "input-email").send_keys(new_email + "@test.cz")

@then("I should get an error with saying that the email is already registered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(context.driver.find_element(By.CSS_SELECTOR, "#alert > div > i").text)# == " Warning: E-Mail Address is already registered! "


@given("I am logged out")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    open_my_account_menu(context.driver)
    context.driver.find_element(By.LINK_TEXT, "Logout").click()