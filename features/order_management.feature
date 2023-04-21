Feature: Managing orders from the administration perspective

  Scenario: I can log in as admin user
    Given I am at the admin registration page
    And I enter admin login data to the form
    When I press login button
    Then I will be logged in as admin

  Scenario: Admin can create an order
    Given I am at the order page
      And I click add order
      And I fill in necessary data
      When I click confirm order
      Then The order will be added

#    Included in above scenario
#    FIXME: Is unstable.
#    Scenario: Admin can add item to order
#        Given I am at an existing order page
#        And The order has 1 item
#        When I click 'Add item' button
#        And Select an item from the dropdown
#        Then The selected item should appear in the order item list
#        And The list should show 2 items
#
#    Included in above scenario
#    Scenario: Admin can change the shipping address of an order
#        Given I am at an existing order page
#        And I open the 'Shipping Address' detail by clicking the 'Options' button
#        And I enter 'Olomoucká 90' into the Address 1 field
#        When I click the save button
#        Then The address should be set to 'Olomoucká 90'
#        And I should see the 'Success: Shipping address has been set!' popup
#
#
#
    Scenario: Admin can delete an order completely
        Given I am at the order list page
        And At least 1 order is present
        And I select a order
        When I press the 'Delete' button and confirm the alert
        Then I should see a confirmation alert
        And After confirming it the order should be deleted

##    Needs feedback - not sure if this is desired behaviour.
##    Scenario: Admin should not be able to remove the only item on the order list
##        Given I am at an existing order page
##        And The order has only 1 item
##        When I click the 'Remove' button of said item
##        Then An error popup should appear saying that 'It's the only item and cannot be removed
##        And The item should stay in the order list