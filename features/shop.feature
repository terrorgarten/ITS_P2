Feature: Product ordering and manipulation for logged in users
	Background: 
		Given logged in as 'xkonop03@vutbr\.cz'
		And 'xkonop03@vutbr\.cz' is user account
	
	Scenario: Customer adds an item from the homepage to the shopping cart
		Given I am at the homepage 
		And I can see product 'iPhone' in the featured section
		When I click 'Add to cart' on the iPhone card
		Then I should see popup saying 'Success: You have added iPhone to your shopping cart!'
		And I can see that the 'iPhone' was added to the shopping cart
		And I can close the popup

	Scenario: Customer adds 'Canon EOS 5D' in 'Red' variation to the cart
		Given I am at the 'Canon EOS 5D' detail page
		And I select 'Red' from the available options
		When I click 'Add to cart'
		Then I should see popup saying 'Success: You have added 'Canon EOS 5D' to your shopping cart!'
		And I can click 'Exit' on the popup
		And I can see the 'Canon EOS 5D' in 'Red' variation in my shopping cart
		

	Scenario: Customer adds 'iPhone' to the wishlist
		Given I am at the homepage
		And I can see product 'iPhone' in the featured section
		When I click 'Add to wishlist' on the iPhone card
		Then I sould see a 'iPhone' in my wishlist
		And I can see the popup saying Success: 'You have added iPhone to your wishlist'
		And I can close the popup
	
	Scenario: Customer adds 'iMac' and 'MacBook' to the comparison and decides to add the 'iMac' to the cart 
		Given I am at the Apple brand page
		And I can see product 'iMac' and 'MacBook'
		And I don't have any items in my product comparison
		And I add 'iMac' and 'MacBook' to the comparation by clicking the 'Compare this product'
		When I go the product comparison page
		Then I should see 'iMac' and 'Macbook'
		
	Scenario: Customer adds two of the same product to the comparison
		Given I am at the 'iMac' product site
		And I have 'iMac' already in my comparison list
		When I add 'iMac' again
		Then I should only see 1 instance of 'iMac' product on the product comparison page

	Scenario: Customer adds a review
		Given I am at the 'iMac' product site
		And I have the 'Reviews' tab open
		When I add review which has at least 25 characters of text
		And the webmaster confirms this review
		Then I should see the review on the 'iMac' site
 
	Scenario: Customer searches for a product 'iMac' in all categories
		Given I am at the homepage
		And 'iMac' product is present in the system
		And I search for 'iMac' in the top search bar
		When I click the search button
		Then I should see 'iMac' product in the search results

	Scenario: Customer searches for a nonexistent product in given category
		Given I am at the search page
		And 'iMac' product is present in the system with desktop category
		And 'Cameras' is a category which does not apply to 'iMac' product
		When I enter 'iMac' in the search field 
		And I enter 'Cameras' in the category picker
		Then I should not see the 'iMac' product in the search results
			
	Scenario: Customer searches for all products of Apple brand
		Given 'iMac' product exists in the system
		And 'Apple' brand exists in the system
		And 'iMac' product belongs to the 'Apple' brand
		And I am at the 'iMac' detail page
		When I click the 'Apple' button in the Brand row in details
		Then I should see a page with all 'Apple' brand products in the system
		
	Scenario: Customer sorts products by price
		Given I am at the 'Phones & PDAs' page 
		And I can see at least 2 phone products with different price
		When I select 'Price (Low > High)' from the 'Sort by' picker
		Then I should see the cheapest product first
		And I should see the most expensive product at the bottom
	
	Scenario: Customer can edit the quantity of products in their cart
		Given I am at the shoping cart page
		And I have one 'iMac' product in my cart
		When I enter '2' in the quantity column 
		And I click refresh
		Then I will see that I have 2 products in my cart
		And I should see that the price doubled
	
	Scenario: Customer can remove a product from their cart
		Given I am at the shopping cart page
		And I have just one product in my cart
		When I click the remove button
		Then my cart will be empty
		And I will see a popup message saying 'Success: You have removed an item form your shopping list'
		And I will be able to quit the message by pressing the cross

	Scenario: Customer places an order for product in their shopping card
		Given I have a product in my shopping cart
		And I'm at the checkout page
 		And I filled in all credentials correctly
		And I selected a valid payment method
		And I selected a valid shipping method
		And The payment method does not experience any problem and passes
		When I click confirm order
		Then I should see the confirmed order in my account Order History
		And I should see a popup saying 'Success: Your order has been placed'
		And I should be able to quit the popup 

