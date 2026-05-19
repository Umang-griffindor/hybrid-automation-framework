from pathlib import Path


def test_file_download(page):

    html_path = (
        Path(__file__)
        .parent.parent
        / "test_pages"
        / "download_demo.html"
    )

    page.goto(
        f"file://{html_path}"
    )

    download_link = page.locator(
        "#download-link"
    )

    assert download_link.is_visible()

    href_value = download_link.get_attribute(
        "href"
    )

    print(
        f"Download href: "
        f"{href_value}"
    )

    assert (
        href_value
        == "sample_download.txt"
    )