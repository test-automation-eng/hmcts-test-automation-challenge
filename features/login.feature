Feature: Login

    As a registered user
    I want to log in to the application
    So that I can access my account
  
    Background:
      Given I am on the login page
  
    Scenario: Successful login with valid credentials
      When I log in with valid credentials
      Then I should be logged in successfully
  
    Scenario: Login fails with locked credentials
      When I log in with locked user credentials
      Then I should see an account locked error message
    
    Scenario: Login fails with invalid credentials
      When I log in with invalid credentials
      Then I should see a required username field error message

    Scenario: Login fails when username is not selected
      When I attempt to login without selecting a username
      Then I should see a required username field error message 

    Scenario: Login fails when password is not selected
      When I attempt to login without selecting a password
      Then I should see a required password field error message  
  