from pages.base_page import BasePage  # import shared page helper for tab/window handling


def test_multi_tab_handling(page):  # Playwright test for handling a new browser tab

    base_page = BasePage(page)  # instantiate BasePage wrapper for reusable helpers

    page.goto(
        "https://the-internet.herokuapp.com/windows"
    )  # open the page that triggers a new browser window

    new_page = (
        base_page.wait_for_new_tab(

            lambda:
            page.locator(
                "text=Click Here"
            ).click()
        )
    )  # use Playwright expect_popup to wait for the new tab before clicking

    assert (
        "New Window"
        in new_page.locator("h3").text_content()
    )  # assert that the new tab contains the expected page heading