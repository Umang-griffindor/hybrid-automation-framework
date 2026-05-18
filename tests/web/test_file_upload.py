from pathlib import Path
from pages.base_page import BasePage


def test_file_upload(page):

    base_page = BasePage(page)

    html_path = (
        Path(__file__)
        .parent.parent
        / "test_pages"
        / "file_upload_demo.html"
    )

    page.goto(
        f"file://{html_path}"
    )

    file_path = (
        Path(__file__)
        .parent.parent.parent
        / "test_data"
        / "files"
        / "sample_upload.txt"
    )

    base_page.upload_file(
        "#file-upload",
        str(file_path)
    )

    uploaded_file = page.locator(
        "#file-upload"
    ).input_value()

    assert (
        "sample_upload.txt"
        in uploaded_file
    )