from pathlib import Path  # Python import for filesystem path manipulation in a platform-independent way


def test_shadow_dom(page):  # pytest test function validating Playwright shadow DOM handling

    file_path = (
        Path(__file__)
        .parent.parent
        / "test_pages"
        / "shadow_dom_demo.html"
    )  # build local file path to the demo HTML page using Python Path syntax

    page.goto(
        f"file://{file_path}"
    )  # Playwright goto loads the local HTML file into the browser

    shadow_button = page.locator(
        "#host"
    ).locator(
        "#shadow-button"
    )  # access nested shadow DOM element using chained Playwright locators

    assert shadow_button.is_visible()  # assert statement verifies the shadow DOM button is visible