from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import urllib.request
import time

# Playwright is used to simulate mouse clicks and screen scrolling
# Allows us to trigger JavaScript and capture hidden HTML sections
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://uscinteractionlab.web.app/about/people")
    time.sleep(2)   # Allow time for page to load
    page.mouse.wheel(delta_x=0,delta_y=500) # Simulates scrolling to PhD students section
    time.sleep(2)   # Allow time for page to scroll
    page.mouse.click(213,500) # Click on coordinates which are relative to scrolling
    time.sleep(2)   # Allow time for student card to load
    html = page.content() # Capture page HTML
    browser.close()

soup = BeautifulSoup(html,'html.parser')

print(soup.prettify())

'''''
body_tag = soup.body.div.div.p
print(body_tag.prettify())
text = body_tag.contents[0]
print(text)'''