from behave import *
from utils import *

use_step_matcher("re")
new_product_name = "..Product"
edited_product_name = "....ProductEdited"

@given("I am at the admin products page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.LINK_TEXT, "Catalog").click()
    context.driver.find_element(By.LINK_TEXT, "Products").click()

@step("I click the 'Add Item' button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, ".btn > .fa-plus").click()


@step("I fill in the product image, name, meta tag title and SEO keyword")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global new_product_name
    context.driver.find_element(By.ID, "input-name-1").send_keys(new_product_name)
    context.driver.find_element(By.ID, "input-meta-title-1").send_keys("Metatag")
    context.driver.find_element(By.LINK_TEXT, "Data").click()
    context.driver.find_element(By.ID, "input-model").send_keys("Model")
    context.driver.find_element(By.LINK_TEXT, "SEO").click()
    context.driver.find_element(By.ID, "input-keyword-0-1").send_keys(get_random_string(10))


@when("I click the save button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > div > button").click()
    sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then("The item should be added to the product list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global new_product_name
    assert context.driver.find_element(By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr[1]/td[3]').text.split()[0] == new_product_name


######################################################x


@when("I click 'Edit Item' button on the freshly added product")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr[1]/td[7]/div/a').click()

@step("I change the name of the product")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global edited_product_name
    context.driver.find_element(By.ID, "input-name-1").clear()
    context.driver.find_element(By.ID, "input-name-1").send_keys(edited_product_name)

@step("I change the price to a NaN value")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.LINK_TEXT, "Data").click()
    context.driver.find_element(By.ID, "input-price").send_keys("XYZ")



@then("I should see that the item name changed in the list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global edited_product_name
    assert context.driver.find_element(By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr[1]/td[3]').text.split()[0] == edited_product_name


######################################################################


@step("I can see a product on the list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global edited_product_name
    assert context.driver.find_element(By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr[1]/td[3]').text.split()[
               0] == edited_product_name


@when("I click the delete button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > div > button.btn.btn-danger").click()

@then("I should see that the marked products were removed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    sleep(2)
    assert context.driver.find_element(By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr[1]/td[3]').text.split()[
               0] != edited_product_name


@when("I select this item")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, '#form-product > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(1) > input').click()


@step("I confirm the deletion")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.switch_to.alert.accept()
