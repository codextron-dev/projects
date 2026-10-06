# pip install playwright
# python -m playwright install

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.selenium.dev/selenium/web/web-form.html")

    page.fill("input[name='my-text']", "John Doe")
    page.fill("input[name='my-password']", "securepass123")
    page.fill("textarea[name='my-textarea']", "This form was filled automatically!")
    page.select_option("select[name='my-select']", "2")

    page.click("button[type='submit']")

    page.wait_for_timeout(3000)
    browser.close()
    