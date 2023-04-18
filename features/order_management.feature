Feature: Managing orders from the administration perspective
    Background:
        Given logged in as 'user'
        And 'user' is administration account

    Scenario: Admin can add item to order
        Given I am at an existing order page
        And The order has 1 item
        When I click 'Add item' button
        And Select an item from the dropdown
        Then The selected item should appear in the order item list
        And The list should show 2 items

    Scenario: Admin can remove item from order
        Given I am at an existing order page
        And The order has at least 2 item
        When I click 'Remove' button
        Then I should only see 1 item
        And The item should be one that I deleted

    # Could be defined otherwise, but personally consider this the best approach
    Scenario: Admin should not be able to remove the only item on the order list
        Given I am at an existing order page
        And The order has only 1 item
        When I click the 'Remove' button of said item
        Then An error popup should appear saying that 'It's the only item and cannot be removed
        And The item should stay in the order list


    Scenario: Admin can confirm the order
        Given I am at an existing order page
        And The order has items in it
        And The shipping method is set to 'Flat shipping rate'
        And The payment method is set to 'Cash on delivery'
        And The shipping address has been filled correctly
        When I click the confirm button
        Then A message should appear saying 'Success: You have modified orders'

    Scenario: Customer will get notified when admin changes the order status
        Given I am at an existing order page
        And The order has status set as 'Pending'
        When I change the order status from 'Pending' to 'Shipped'
        And I add a comment 'Has been shipped'
        And I click the 'Add history' button
        Then The customer should be notified
        And I should see the comment and status update in the order history list
        And Status should be changed to 'Shipped'
        And I should see a popup saying 'Success: You have modified orders'

    Scenario: Admin can add reward points
        Given I am at an existing order page
        And I have the 'More' option open
        When I click the '+' button next to reward points
        Then I should see 'Success: Reward points added' popup
        And The customer owning this order should recieve their points


    Scenario: Admin can change the shipping address of an order
        Given I am at an existing order page
        And I open the 'Shipping Address' detail by clicking the 'Options' button
        And I enter 'Olomoucká 90' into the Address 1 field
        When I click the save button
        Then The address should be set to 'Olomoucká 90'
        And I should see the 'Success: Shipping address has been set!' popup

    Scenario: Admin can print the invoice
        Given I am at the order list page
        And I can see at least 1 order
        And I select 1 order
        When I click the 'Print invoice' button
        Then I should be redirected to another panel with the invoice

    Scenario: Admin can print the shipping list with multiple orders
        Given I am at the order list page
        And I at least 2 orders are present
        And I select all the orders
        When I click 'Print shipping list' button
        Then I should be redirected to another panel with the dispach notes
        And 2 dispach notes should be available

    Scenario: Admin can delete an order completely
        Given I am at the order list page
        And At least 1 order is present
        And I select a order
        When I press the 'Delete' button
        Then I should see a confirmation alert
        And After confirming it the order should be deleted