def test_iframe_interaction(page):  # Playwright test for interacting with a page iframe

    page.goto(
        "https://demoqa.com/frames"
    )  # open the demo frames page with Playwright

    frame = page.frame_locator(
        "#frame1"
    )  # locate the iframe using Playwright frame locator syntax

    heading = frame.locator(
        "#sampleHeading"
    )  # locate an element inside the iframe context

    assert (
        "This is a sample page"
        in heading.text_content()
    )  # verify the iframe content text is present