Feature: Managing user accounts from administration perspective
    Background:
        Given logged in as 'user'
        And 'user' is administration account

    Scenario: Admin can create new user
        Given I am on the customers page
        And There is no user under email 'test@test¨cz
        When I click the 'Add' button
        And I fill in the first name, last name, email 'test@test.cz', password and password confirmation with at least 4 characters
        Then New user account should be created and visible in the customer list


    Scenario: Admin can edit user information
        Given I am at the customers page
        And There is at least one user account
        When I click the 'Edit' button
        And I change the first name to 'new-name'
        And click the 'Save' button
        Then I should see that the first name has changed to 'new-name' by this account

    Scenario: Admin can remove user account
        Given I am at the customers page
        And There is at least one user account
        When I select the account by ticking it
        And I click on 'Delete' button
        Then A confirmation button should popup
        And The account should be deleted after confirmation

    Scenario Admin cannot create a user with an email that is already taken
        Given I am on the customers page
        And There already is user under email 'test@test' in the system
        When I click the 'Add' button
        And I fill in the first name, last name, email 'test@test.cz', password and password confirmation with at least 4 characters
        Then An error saying 'Warning: E-mail address is already registered'