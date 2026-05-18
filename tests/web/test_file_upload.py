from pathlib import Path  # Python import to build file paths to local test resources
from pages.base_page import BasePage  # import base page helper with file upload support


def test_file_upload(page):  # Playwright test that validates file upload behavior

    base_page = BasePage(page)  # instantiate BasePage with the Playwright page object

    html_path = (
        Path(__file__)
        .parent.parent
        / "test_pages"
        / "file_upload_demo.html"
    )  # resolve the demo HTML page path using pathlib

    page.goto(
        f"file://{html_path}"
    )  # open the local file upload demo page in the browser

    file_path = (
        Path(__file__)
        .parent.parent.parent
        / "test_data"
        / "files"
        / "sample_upload.txt"
    )  # resolve the path to the sample file used for upload

    base_page.upload_file(
        "#file-upload",
        str(file_path)
    )  # call reusable upload helper from BasePage

    uploaded_file = page.locator(
        "#file-upload"
    ).input_value()  # read the selected file name from the upload control

    assert (
        "sample_upload.txt"
        in uploaded_file
    )  # verify that the correct file was selected for upload