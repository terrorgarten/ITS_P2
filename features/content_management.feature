Feature: Managing items in the store

    Scenario: I can log in as admin user
        Given I am at the admin registration page
        And I enter admin login data to the form
        When I press login button
        Then I will be logged in as admin

    Scenario: Adding item to the product list
        Given I am at the admin products page
        And I click the 'Add Item' button
        And I fill in the product image, name, meta tag title and SEO keyword
        When I click the save button
        Then The item should be added to the product list

    Scenario: Editing an item in the product list
        Given I am at the admin products page
        When I click 'Edit Item' button on the freshly added product
        And I change the name of the product
        #And I change the price to a NaN value
        And I click the save button
        Then I should see that the item name changed in the list

    Scenario: Deleting product from the product list
        Given I am at the admin products page
        And I can see a product on the list
        When I select this item
        And I click the delete button
        And I confirm the deletion
        Then I should see that the marked products were removed
