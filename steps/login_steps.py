from pytest_bdd import given, when, then
from pages.login_page import LoginPage
from config.settings import (
    VALID_USERNAME,
    VALID_PASSWORD,
    LOCKED_USERNAME,
    LOCKED_PASSWORD,
)


# ---------- GIVEN ----------

@given("I am on the login page")
def open_login_page(page):
    LoginPage(page).open()


# ---------- WHEN ----------

@when("I log in with valid credentials")
def login_with_valid_credentials(page):
    LoginPage(page).login(VALID_USERNAME, VALID_PASSWORD)


@when("I log in with locked user credentials")
def login_with_locked_user(page):
    LoginPage(page).login(LOCKED_USERNAME, VALID_PASSWORD)


@when("I log in with invalid credentials")
def login_with_invalid_credentials(page):
    LoginPage(page).login("testuser", "testpassword")


@when("I attempt to login without selecting a username")
def login_without_username(page):
    LoginPage(page).login_without_username(VALID_PASSWORD)

@when("I attempt to login without selecting a password")
def login_without_password(page):
    LoginPage(page).login_without_password(VALID_USERNAME)


# ---------- THEN ----------

@then("I should be logged in successfully")
def verify_successful_login(page):
    assert LoginPage(page).is_logged_in(), (
        "Expected user to be logged in, but login was unsuccessful"
    )


@then("I should see an account locked error message")
def verify_account_locked_error(page):
    error_message = LoginPage(page).get_error_message()
    assert error_message == "Your account has been locked.", (
        f"Unexpected error message displayed: {error_message}"
    )


@then("I should see a required username field error message")
def verify_required_username_error(page):
    error_message = LoginPage(page).get_error_message()
    assert error_message == "Invalid Username", (
        f"Unexpected error message displayed: {error_message}"
    )


@then("I should see a required password field error message")
def verify_required_password_error(page):
    error_message = LoginPage(page).get_error_message()
    assert error_message == "Invalid Password", (
        f"Unexpected error message displayed: {error_message}"
    )
