def test_iframe_interaction(page):

    page.goto(
        "https://demoqa.com/frames"
    )

    frame = page.frame_locator(
        "#frame1"
    )

    heading = frame.locator(
        "#sampleHeading"
    )

    assert (
        "This is a sample page"
        in heading.text_content()
    )