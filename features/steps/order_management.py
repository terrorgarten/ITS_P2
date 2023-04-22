from behave import *
from utils import *

use_step_matcher("re")
deleted_order_id = ""

@given("I am at the order page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.LINK_TEXT, "Sales").click()
    context.driver.find_element(By.LINK_TEXT, "Orders").click()


@step("I click add order")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()


@step("I fill in necessary data")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, ".row-cols-1 > .col:nth-child(2) .btn").click()
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("Matěj")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Konopík")
    context.driver.find_element(By.ID, "input-email").send_keys("matejkonopik@gmail.com")
    context.driver.find_element(By.ID, "input-telephone").send_keys("728 521 885")
    context.driver.find_element(By.CSS_SELECTOR, "#button-customer").click()
    context.driver.find_element(By.CSS_SELECTOR, "#modal-customer .btn-close").click()


    context.driver.find_element(By.CSS_SELECTOR, "#content > div.container-fluid > div:nth-child(1) > div.card-body > table:nth-child(2) > tfoot > tr > td.text-end > button").click()
    context.driver.find_element(By.ID, "input-product").send_keys("i")
    context.driver.find_element(By.ID, "input-product").send_keys("M")
    context.driver.find_element(By.ID, "input-product").send_keys("a")
    context.driver.find_element(By.ID, "input-product").send_keys("c")
    WebDriverWait(context.driver, 2)
    sleep(1)
    context.driver.find_element(By.ID, "button-product-add").click()
    context.driver.find_element(By.CSS_SELECTOR, "#modal-cart .btn-close").click()


    context.driver.find_element(By.CSS_SELECTOR, "#shipping-address .btn").click()
    context.driver.find_element(By.ID, "input-shipping-firstname").click()
    context.driver.find_element(By.ID, "input-shipping-firstname").send_keys("Jan")
    context.driver.find_element(By.ID, "input-shipping-lastname").send_keys("Kop")
    context.driver.find_element(By.ID, "input-shipping-address-1").send_keys("Možná")
    context.driver.find_element(By.ID, "input-shipping-city").send_keys("Brno")
    context.driver.find_element(By.ID, "input-shipping-postcode").send_keys("66600")
    context.driver.find_element(By.ID, "input-shipping-country").click()
    select1 = Select(context.driver.find_element(By.ID, "input-shipping-country"))
    select1.select_by_value("1")
    sleep(1)
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="input-shipping-zone"]')))
    select2 = Select(context.driver.find_element(By.XPATH,'//*[@id="input-shipping-zone"]'))
    select2.select_by_value("10")
    context.driver.find_element(By.XPATH, '//*[@id="button-shipping-address"]').click()
    context.driver.find_element(By.CSS_SELECTOR, "#modal-shipping-address .btn-close").click()

    context.driver.find_element(By.XPATH, '//*[@id="button-shipping-method"]').click()
    context.driver.find_element(By.XPATH, '//*[@id="button-payment-method"]').click()

    select_ship_method = Select(context.driver.find_element(By.XPATH, '//*[@id="input-shipping-method"]'))
    select_pay_method  = Select(context.driver.find_element(By.XPATH, '//*[@id="input-payment-method"]'))

    select_ship_method.select_by_value("flat.flat")
    select_pay_method.select_by_value("cod")


@when("I click confirm order")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    element = context.driver.find_element(By.ID, "button-confirm")
    context.driver.execute_script("arguments[0].click();", element)

@then("The order will be added")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    sleep(1)
    assert context.driver.find_element(By.CSS_SELECTOR, "#alert > div").text == "Success: You have modified orders!"



####################################################################


@given("I am at the order list page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > div > a.btn.btn-light").click()


@step("At least 1 order is present")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global deleted_order_id
    deleted_order_id = context.driver.find_element(By.XPATH, '//*[@id="form-order"]/div[1]/table/tbody/tr[1]/td[2]').text
@step("I select a order")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.XPATH, '//*[@id="form-order"]/div[1]/table/tbody/tr[1]/td[1]/input[1]').click()


@when("I press the 'Delete' button and confirm the alert")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.ID, 'button-delete').click()
    context.driver.switch_to.alert.accept()


@then("I should see a confirmation alert")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver.find_element(By.CSS_SELECTOR, "#alert > div").text == "Success: You have modified orders!"

@step("After confirming it the order should be deleted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global deleted_order_id
    assert context.driver.find_element(By.XPATH, '//*[@id="form-order"]/div[1]/table/tbody/tr[1]/td[2]').text != deleted_order_id
