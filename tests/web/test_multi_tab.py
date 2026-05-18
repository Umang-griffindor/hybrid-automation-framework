from pages.base_page import BasePage


def test_multi_tab_handling(page):

    base_page = BasePage(page)

    page.goto(
        "https://the-internet.herokuapp.com/windows"
    )

    new_page = (
        base_page.wait_for_new_tab(

            lambda:
            page.locator(
                "text=Click Here"
            ).click()
        )
    )

    assert (
        "New Window"
        in new_page.locator("h3").text_content()
    )