import os  # Python import for filesystem checks and directory creation
import pytest  # Python import for pytest fixtures and test lifecycle hooks


@pytest.hookimpl(hookwrapper=True)  # pytest hook decorator, wraps test reporting logic
def pytest_runtest_makereport(item, call):  # Python function used by pytest to collect test results

    outcome = yield  # yield syntax in pytest hookwrapper to let pytest execute the test first

    rep = outcome.get_result()  # retrieve the report object produced by pytest

    setattr(item, "rep_" + rep.when, rep)  # Python reflection to store report metadata on the test item


"""@pytest.fixture(scope="function")
def browser_page(browser):

    page = browser.new_page()

    yield page

    page.close()"""  # commented-out fixture example for Playwright browser page setup


@pytest.fixture(autouse=True)  # pytest fixture syntax to automatically apply this fixture
def screenshot_on_failure(request, page):  # fixture receives request and Playwright page objects

    yield  # yield control to the test body, then resume after the test finishes

    if hasattr(request.node, "rep_call"):  # Python hasattr checks if the test report exists

        if request.node.rep_call.failed:  # branch to handle failed tests only

            screenshots_dir = "screenshots"  # string assignment for screenshot directory

            if not os.path.exists(screenshots_dir):  # Python check to ensure directory exists

                os.makedirs(screenshots_dir)  # create directory if missing for screenshot output

            screenshot_path = (
                f"{screenshots_dir}/{request.node.name}.png"
            )  # formatted string with test name for screenshot file path

            page.screenshot(path=screenshot_path)  # Playwright API to capture a screenshot on failure

            print(f"\nScreenshot saved: {screenshot_path}")  # Python print for console feedback

@pytest.fixture
def login_page(page):

    from pages.login_page import LoginPage

    login_page = LoginPage(page)

    login_page.open_login_page()

    return login_page