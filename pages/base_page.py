from playwright.sync_api import Page


class BasePage:
    """
    Base Page providing common Playwright helper methods.
    Keeps abstraction light and reusable.
    """

    def __init__(self, page: Page):
        self.page = page

    def click(self, selector: str):
        """Click an element."""
        self.page.locator(selector).click()

    def wait_for_visible(self, selector: str, timeout: int = 5000):
        """Wait for an element to become visible."""
        self.page.locator(selector).wait_for(state="visible", timeout=timeout)

    def get_text(self, selector: str) -> str:
        """Return visible text content of an element."""
        return self.page.locator(selector).text_content().strip()

    def click_by_text(self, selector_template: str, value: str):
        """
        Click an element using a formatted selector.
        """
        self.page.locator(selector_template.format(value=value)).click()    
