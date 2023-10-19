from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import urllib.request

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://uscinteractionlab.web.app/about/peoplep")
    html = page.content()
    browser.close()

soup = BeautifulSoup(html,'html.parser')

print(soup.prettify())
'''''
body_tag = soup.body.div.div.p
print(body_tag.prettify())
text = body_tag.contents[0]
print(text)'''