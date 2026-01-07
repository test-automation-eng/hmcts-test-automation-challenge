import pytest
from playwright.sync_api import sync_playwright

pytest_plugins = ["steps.login_steps"]


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to run tests against: chromium, firefox, webkit",
    )

    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run browser in headed mode",
    )

@pytest.fixture
def page(request):
    """
    Provides a Playwright page instance for each test.
    Ensures browser is properly started and closed.
    """
    browser_name = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")

    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=not headed)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=not headed)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=not headed)
        else:
            raise ValueError(
                f"Unsupported browser '{browser_name}'. "
                "Use: chromium, firefox, or webkit."
            )

        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path="reports/failure.png")        
