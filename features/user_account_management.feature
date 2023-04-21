Feature: Managing user accounts from administration perspective

    Scenario: I can log in as admin user
        Given I am at the admin registration page
        And I enter admin login data to the form
        When I press login button
        Then I will be logged in as admin

    Scenario: Admin can create new user
        Given I am on the customers page
        When I click the 'Add' button
        And I fill in the first name, last name, email, password and password confirmation with at least 4 characters
        And I click 'Save' button
        And I click 'Return' button
        And I search for user by their email
        Then User account should be visible in the customer list

    Scenario: Admin can search for user by their name
        Given I am on the customers page
        When I search for user by their email
        Then User account should be visible in the customer list

    Scenario: Admin cannot create a user with an email that is already taken
        Given I am on the customers page
        And I search for user by their email
        And User account should be visible in the customer list
        When I click the 'Add' button
        And I fill in the first name, last name, same email, password and password confirmation with at least 4 characters for the existing user
        And I click 'Save' button
        Then An error saying 'Warning: E-mail address is already registered'

    Scenario: Admin can edit user information
        Given I am on the customers page
        When I click the 'Edit' button on some user
        And I change the email
        And I click the 'Save' button
        # differs, different css identifiers than create user return button
        And I click the 'Return' button on edit page
        Then I and search out the changed account
        And The account with new email should be visible

    Scenario: Admin can remove user account
        Given I am on the customers page
        When I search out the edited account by email
        And I select account by ticking it
        And I click on 'Delete' button
        Then A confirmation button should popup and I confirm it
        And The account should be deleted after confirmation