from pathlib import Path


def test_shadow_dom(page):

    file_path = (
        Path(__file__)
        .parent.parent
        / "test_pages"
        / "shadow_dom_demo.html"
    )

    page.goto(
        f"file://{file_path}"
    )

    shadow_button = page.locator(
        "#host"
    ).locator(
        "#shadow-button"
    )

    assert shadow_button.is_visible()