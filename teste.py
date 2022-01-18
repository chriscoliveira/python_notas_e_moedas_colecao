from playwright.sync_api import sync_playwright
from time import sleep
URL = 'https://pt.ucoin.net/uid26638?v=home'
with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    page.goto(URL)
    page.click('#cookies-warning > div > div.right > div')
    # page.query_selector(id="map")
#    sleep(8)
    page.click('#map')

    page.locator(
        '#user-map > div.modal-container > div.modal-body').screenshot(path="screenshot.png")
    browser.close()
