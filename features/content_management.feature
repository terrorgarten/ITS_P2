Feature: Managing items in the store
    Background:
        Given logged in as 'user'
        And 'user' is administration account

    Scenario: Adding item to the product list
        Given I am at the admin products page
        And I click the 'Add Item' button
        And I fill in the product image, name, meta tag title and SEO keyword
        When I click the save button
        Then The item should be added to the product list
        And The item should contain the entered image, name, meta tag title and SEO keyword

    Scenario: Editing an item in the product list
        Given I am at the admin products page
        And I can see at least 1 product on the list
        When I click 'Edit Item' button
        And I change the name of the product to 'New product'
        And I click the save button
        Then I should see that the item name changed in the list

    Scenario: Editing the quantity of a product
        Given I am the admin products page
        And I can see a product with 10 quantity
        When I click the edit button
        And I navigate to the Data page
        And I change the quantity to 20
        And I click the 'Save' button
        Then I should see that the product quantity is 20 on the list

    Scenario: Deleting multiple products from the product list
        Given I am at the admin products page
        And I can see at least 2 product on the list
        When I mark 2 products
        And I click the delete button
        Then I should see that the marked products were removed

    Scenario: Adding a product variant
        Given I am at the admin products page
        And I can see at least 1 product on the list
        When I click the dropdown next to edit
        And I select add variant
        And I add new attribute 'color' with value 'red'
        And I change the SEO keyword to 'xxx'
        And I click the save button
        Then I should see that variation has been created in the product list
        And I should see that it contains the entered data