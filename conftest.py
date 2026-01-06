import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    """
    Provides a Playwright page instance for each test.
    Ensures browser is properly started and closed.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()
