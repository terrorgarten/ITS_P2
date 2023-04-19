Feature: Product ordering and manipulation for logged in users

	Scenario: User can log in
		Given I type in my credentials
		When I click enter
		Then I will see my email in the manager page

	Scenario: Customer adds an item from the homepage to the shopping cart
		Given I am at the homepage
		And I can see product 'iPhone' in the featured section
		When I add iPhone to the cart
		Then I can see that the 'iPhone' was added to the shopping cart

	Scenario: Customer removes iPhone from the cart
		Given I can see iPhone in my cart
		When I click Remove iPhone from the cart
		Then I can see that the iPhone was removed from the cart

	Scenario: Customer adds 'Canon EOS 5D' in 'Red' variation to the cart
		Given I am at the 'Canon EOS 5D' detail page
		And I select 'Red' from the available options
		When I click 'Add to cart'
		Then I can see the 'Canon EOS 5D' in 'Red' variation in my shopping cart

	Scenario: Customer searches for a product 'iMac' in all categories
		Given I search for 'iMac' in the top search bar
		When I click the search button
		Then I should see 'iMac' product in the search results

	# FIXME - cannot add payment method, cannot create order as user !!!
#	Scenario: Customer places an order for product in their shopping cart
#		Given I have a product in my shopping cart
#		And I'm at the checkout page
#		And I filled in all credentials correctly
#		And I selected a valid payment method
#		And I selected a valid shipping method
#		And The payment method does not experience any problem and passes
#		When I click confirm order
#		Then I should see the confirmed order in my account Order History
#		And I should see a popup saying 'Success: Your order has been placed'
#		And I should be able to quit the popup

# -------------- EXCLUDED: ----------------------------------------------------------------
#	Scenario: Customer adds 'iPhone' to the wishlist
#		Given I am at the homepage
#		And I can see product 'iPhone' in the featured section
#		When I click 'Add to wishlist' on the iPhone card
#		Then I sould see a 'iPhone' in my wishlist
#		And I can see the popup saying Success: 'You have added iPhone to your wishlist'
#		And I can close the popup
#
#	Scenario: Customer adds a review
#		Given I am at the 'iMac' product site
#		And I have the 'Reviews' tab open
#		When I add review which has at least 25 characters of text
#		And the webmaster confirms this review
#		Then I should see the review on the 'iMac' site
#
#	Scenario: Customer searches for a product 'iMac' in all categories
#		Given I am at the homepage
#		And 'iMac' product is present in the system
#		And I search for 'iMac' in the top search bar
#		When I click the search button
#		Then I should see 'iMac' product in the search results
#
#	Scenario: Customer sorts products by price
#		Given I am at the 'Phones & PDAs' page
#		And I can see at least 2 phone products with different price
#		When I select 'Price (Low > High)' from the 'Sort by' picker
#		Then I should see the cheapest product first
#		And I should see the most expensive product at the bottom
#
#	Scenario: Customer can edit the quantity of products in their cart
#		Given I am at the shoping cart page
#		And I have one 'iMac' product in my cart
#		When I enter '2' in the quantity column
#		And I click refresh
#		Then I will see that I have 2 products in my cart
#		And I should see that the price doubled


