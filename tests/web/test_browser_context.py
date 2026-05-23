def test_browser_contexts(browser):

    context_1 = browser.new_context()

    context_2 = browser.new_context()

    page_1 = context_1.new_page()

    page_2 = context_2.new_page()

    page_1.goto(
        "https://example.com"
    )

    page_2.goto(
        "https://example.com"
    )

    print(
        "Two isolated browser contexts created"
    )

    assert page_1.url == page_2.url

    context_1.close()

    context_2.close()