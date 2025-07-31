from playwright.sync_api import sync_playwright, expect

def test_input_form_submit():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.lambdatest.com/selenium-playground")
        page.click("text=Input Form Submit")
        
        page.click("button:has-text('Submit')")
        
        first_input = page.locator('input[required]').first
        validation_message = first_input.evaluate('el => el.validationMessage')
        assert validation_message == "Please fill out this field."

        page.fill('input[placeholder="Email"]', "test@example.com")
        page.fill('input[placeholder="Name"]', "test@example.com")
        page.fill('input[placeholder="Password"]', "test@example.com")
        page.fill('input[placeholder="Company"]', "test@example.com")
        page.fill('input[placeholder="Website"]', "test@example.com")
        page.fill('input[placeholder="City"]', "test@example.com")
        page.fill('input[placeholder="Address 1"]', "test@example.com")
        page.fill('input[placeholder="Address 2"]', "test@example.com")
        page.fill('input[placeholder="State"]', "test@example.com")
        page.fill('input[placeholder="Zip code"]', "test@example.com")
        page.select_option('select[name="country"]', value="US")
        page.click("button:has-text('Submit')")
        success_msg = page.locator('p.success-msg')
        expected_text = "Thanks for contacting us, we will get back to you shortly."

        assert success_msg.text_content() == expected_text, f"Expected: '{expected_text}', Got: '{success_msg.text_content()}'"
        
        browser.close()

test_input_form_submit()