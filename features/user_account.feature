Feature: User account registration and order history operations
	
	Scenario: User can log out
		Given I am logged in as user
		When I click the logout button
		Then I will be logged out

	Scenario: User can make an account with valid inputs
		Given I am at the register account page 
		And I filled in name
		And I filled in surname
		And I filled in email in a valid format
		And I filled in valid password
		And I agreed to the Privacy Policy
		When I press the register button 
		Then my account should be created in the system

	# Could be moved but it relates to users a bit
	Scenario: System withstand a very weak try for sql injection
		When I enter the injection query
		Then I should get an error page or nothing should happen
	
	Scenario: User can't make an account on email that is already in use
		Given I am logged out
		And I am at the register account page
		And I filled the form with valid data
		And I fill in existing account email
		And I agreed to the Privacy Policy
		When I press the register button
		Then I should get an error with saying that the email is already registered

