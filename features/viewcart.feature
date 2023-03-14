Feature: Add Functionality

  Scenario: Click view cart symbol in view cart
   Given I open application URL in the browser
   Then i click on the view cart tab so it will open

  Scenario: Add products to view cart
   Given I open application URL in the browser
   And i click on search bar to search the paint name
   When i click the paint name it redirects to paint page
   Then product will be added to view cart tab

  Scenario: Remove products in view cart
   Given I open application URL in the browser
   And i click on search bar to search the paint name
   When i click the paint name it redirects to paint page
   Then click on remove button

  Scenario: Increase product quantity in view cart
   Given I open application URL in the browser
   And i click on search bar to search the paint name
   When i click the paint name it redirects to paint page
   Then i click on increase button so, the product quantity will increase

  Scenario: Decrease product quantity in view cart
   Given I open application URL in the browser
   And i click on search bar to search the paint name
   When i click the paint name it redirects to paint page
   Then i click on decrease button so, the product decrease


  Scenario: Click start shopping option in view cart
  Given I open application URL in the browser
  When i click on the view cart tab so it will open
  And i click on start shopping option
  Then it redirects to start shopping page

  Scenario: Checkout option in view cart
  Given I open application URL in the browser
  And i click on search bar to search the paint name
  When i click the paint name it redirects to paint page
  Then i click on checkout option

  Scenario: click on the product in view cart tab, it should redirect to the product page
  Given I open application URL in the browser
  And i click on search bar to search the paint name
  When i click the paint name it redirects to paint page
  Then i click on product so, it redirects to product page

  Scenario: The user can see total amount in the view cart tab.
  Given I open application URL in the browser
  And i click on search bar to search the paint name
  When i click the paint name it redirects to paint page
  Then i can see the total amount in view cart tab
