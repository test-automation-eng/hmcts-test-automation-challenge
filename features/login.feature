Feature: Login

    As a registered user
    I want to log in to the application
    So that I can access my account
  
    Background:
      Given I am on the login page
  
    Scenario: Successful login with valid credentials
      When I log in with valid credentials
      Then I should be logged in successfully
  
    Scenario: Login fails with invalid credentials
      When I log in with invalid credentials
      Then I should see an authentication error message
  