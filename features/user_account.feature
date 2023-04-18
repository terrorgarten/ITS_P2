Feature: User account registration and order history operations
	
	Scenario: User can make an account with valid inputs
		Given I am at the register account page 
		And I filled in name with 'Matěj'
		And I filled in surename 'Konopík'
		And I filled in email in a valid format, eg. 'email@email.cz'
		And I filled in valid password
		And I agreed to the Privacy Policy
		When I press the register button 
		Then my account should be created in the system
	
	Scenario: User can't make an account on email that is already in use
		Given I am at the register account page
		And I filled the form with valid data
		And an account under 'test@test.com' already exists in the system
		And I agreed to the Privacy Policy terms
		And I enter email 'test@test.com' into the form
		When I click the continue button
		Then I should get an error with saying that the email is already registered
	
	Scenario: User can't make an account without agreeing to the Privacy Policy
		Given I am at the register account page
		And I filled all form data correctly
		And I did not tick the checkbox for agreeing to Privacy Policy
		When I click th continue button
		Then I should get an error aletring me to tick the checkbox

	Scenario: Registered user can log in
		Given I have an account correctly registered under 'xkonop03@vutbr.cz'
		And I am at the login page
		And I fill in my credentials
		When I click login
		Then I should be logged in under my account 'xkonop03@vutbr.cz'

	Scenario: User can view his order history
		Given I am logged in
		And I have exactly one order
		And I am at the order history page
		Then I can see my only order
