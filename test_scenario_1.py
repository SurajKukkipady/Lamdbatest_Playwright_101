from playwright.sync_api import sync_playwright, expect

def test_simple_form_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        
        page.goto("https://www.lambdatest.com/selenium-playground")
        page.click("a[href*='simple-form-demo']")

        assert "simple-form-demo" in page.url, "URL validation failed!"

        input_message = "Welcome to LambdaTest"
        page.fill("#user-message", input_message)
        page.click("#showInput")

        output_text = page.text_content("#message")
        assert output_text == input_message, f"Message mismatch! Expected: {input_message}, Got: {output_text}"

        browser.close()

test_simple_form_demo()