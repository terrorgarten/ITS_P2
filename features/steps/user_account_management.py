from behave import *
from utils import *

use_step_matcher("re")
new_user_email = ""
mail_to_change = ""

@given("I am at the admin registration page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("http://mys01.fit.vutbr.cz:8084/administration/")


@step("I enter admin login data to the form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.ID, "input-username").send_keys(ADMIN_USERNAME)
    context.driver.find_element(By.ID, "input-password").send_keys(ADMIN_PASSWORD)

@when("I press login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, ".btn").click()



@then("I will be logged in as admin")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Dashboard"


###############################################


@given("I am on the customers page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.LINK_TEXT, "Customers").click()
    context.driver.find_element(By.CSS_SELECTOR, "#collapse-5 > li:nth-child(1) > a").click()

@when("I click the 'Add' button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > div > a").click()

@step(
    "I fill in the first name, last name, email, password and password confirmation with at least 4 characters")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global new_user_email
    new_user_email = get_random_string(10)
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("TESTINGUSER")
    context.driver.find_element(By.ID, "input-lastname").send_keys("TESTINGUSER")
    context.driver.find_element(By.ID, "input-email").send_keys(new_user_email + "@TEST.EU")
    context.driver.find_element(By.ID, "input-password").send_keys("1234")
    context.driver.find_element(By.ID, "input-confirm").send_keys("1234")


@step("I click 'Save' button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary").click()

@step("I search for user by their email")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global new_user_email
    context.driver.find_element(By.ID, "input-email").send_keys(new_user_email)
    context.driver.find_element(By.ID, "button-filter").click()

@step("User account should be visible in the customer list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver.find_element(By.CSS_SELECTOR, '#form-customer > div.table-responsive > table > tbody > tr > td:nth-child(2)')


#############################################################


@then("An error saying 'Warning: E-mail address is already registered'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver.find_element(By.CSS_SELECTOR, "#alert > div").text == "Warning: E-Mail Address is already registered!"


@step(
    "I fill in the first name, last name, same email, password and password confirmation with at least 4 characters for the existing user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global new_user_email
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("TESTINGUSER")
    context.driver.find_element(By.ID, "input-lastname").send_keys("TESTINGUSER")
    context.driver.find_element(By.ID, "input-email").send_keys(new_user_email + "@TEST.EU")
    context.driver.find_element(By.ID, "input-password").send_keys("1234")
    context.driver.find_element(By.ID, "input-confirm").send_keys("1234")


@step("I click 'Return' button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > div > a").click()


########################################################################

@when("I click the 'Edit' button on some user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.ID, "input-email").send_keys(new_user_email)
    context.driver.find_element(By.ID, "button-filter").click()
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, '#form-customer > div.table-responsive > table > tbody > tr > td.text-end > div > a').click()


@step("I change the email")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global mail_to_change
    mail_to_change = get_random_string(10) + "@testmail.com"
    context.driver.find_element(By.ID, "input-email").clear()
    context.driver.find_element(By.ID, "input-email").send_keys(mail_to_change)

@step("I click the 'Save' button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > div > button").click()


@step("I click the 'Return' button on edit page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > div > a.btn.btn-light").click()


@step("I and search out the changed account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global mail_to_change
    context.driver.find_element(By.ID, "input-email").clear()
    context.driver.find_element(By.ID, "input-email").send_keys(mail_to_change)
    context.driver.find_element(By.ID, "button-filter").click()





@step("The account with new email should be visible")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global mail_to_change
    assert context.driver.find_element(By.CSS_SELECTOR, "#form-customer > div.table-responsive > table > tbody > tr > td:nth-child(3)"). text == mail_to_change



####################################################################x
@when("I search out the edited account by email")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global mail_to_change
    context.driver.find_element(By.ID, "input-email").clear()
    context.driver.find_element(By.ID, "input-email").send_keys(mail_to_change)
    context.driver.find_element(By.ID, "button-filter").click()
@step("I select account by ticking it")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, "#form-customer > div.table-responsive > table > tbody > tr > td.text-center > input").click()
###

@step("I click on 'Delete' button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > div > button.btn.btn-danger").click()


@then("A confirmation button should popup and I confirm it")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # #alert
    context.driver.switch_to.alert.accept()


@step("The account should be deleted after confirmation")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver.find_element(By.CSS_SELECTOR, "#alert > div").text == "Success: You have modified customers!"


