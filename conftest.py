import os
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


"""@pytest.fixture(scope="function")
def browser_page(browser):

    page = browser.new_page()

    yield page

    page.close()"""


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):

    yield

    if hasattr(request.node, "rep_call"):

        if request.node.rep_call.failed:

            screenshots_dir = "screenshots"

            if not os.path.exists(screenshots_dir):

                os.makedirs(screenshots_dir)

            screenshot_path = (
                f"{screenshots_dir}/{request.node.name}.png"
            )

            page.screenshot(path=screenshot_path)

            print(f"\nScreenshot saved: {screenshot_path}")