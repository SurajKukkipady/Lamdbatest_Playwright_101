from playwright.sync_api import sync_playwright

def test_slider():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.lambdatest.com/selenium-playground")
        page.click("text=Drag & Drop Sliders")
        
        slider = page.locator("input[type='range'][value='15']").first
        slider.fill("95")
        
        output_value = page.locator("#rangeSuccess").text_content()
        assert output_value == "95", f"Expected range value 95, got {output_value}"
        
        page.wait_for_timeout(3000)
        browser.close()

test_slider()