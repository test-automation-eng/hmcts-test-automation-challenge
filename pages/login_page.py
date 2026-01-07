import logging
from config.settings import BASE_URL
from pages.base_page import BasePage
logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    """
    Page Object representing the login page of the application.
    Encapsulates all login-related interactions and assertions.
    """

    URL = BASE_URL

    def __init__(self, page):
        super().__init__(page)

        # Locators
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "#login-btn"
        self.error_message = ".api-error"
        self.logout_button = "#signin"
        self.dropdown_option = (
        "//div[contains(@class,'option') and normalize-space(text())='{value}']")
        self.create_option = (
            "//div[contains(@class,'option') and contains(text(),'Create')]"
        )

    def open(self):
        """Navigate to the login page."""
        logger.info("Navigating to login page")
        self.page.goto(self.URL)

    def _select_dropdown_value(self, dropdown_selector: str, value: str):
        """
        Select a value from a react-select dropdown.
        Supports both existing and dynamically created values.
        """
        self.page.locator(dropdown_selector).click()
        input_box = self.page.locator(f"{dropdown_selector} input")
        input_box.fill(value)
        # Try exact match first
        option = self.page.locator(
            self.dropdown_option.format(value=value)
        )

        if option.count() > 0:
            option.first.click()
        else:
            # Fallback to 'Create "value"'
            self.page.locator(self.create_option).first.click()

    def login(self, username: str, password: str):
        """Perform login using react-select dropdowns."""
        logger.info(f"Attempting login with username: {username}")
        # Username selection
        self._select_dropdown_value(self.username_input, username)
        # Password selection
        self._select_dropdown_value(self.password_input, password)
        # Click login button
        self.click(self.login_button) 

    def is_logged_in(self) -> bool:
        """Return True if login was successful."""
        logger.info("Verifying user is logged in")
        try:
            self.wait_for_visible(self.logout_button, timeout=5000)
            return True
        except:
            return False

    def get_error_message(self) -> str:
        logger.info("Reading login error message")
        self.wait_for_visible(self.error_message)
        return self.get_text(self.error_message)

    def login_without_username(self, password: str):
        self._select_dropdown_value(self.password_input, password)
        self.click(self.login_button)

    def login_without_password(self, username: str):
        self._select_dropdown_value(self.username_input, username)
        self.click(self.login_button)    