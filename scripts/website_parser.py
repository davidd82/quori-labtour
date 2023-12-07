from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import urllib.request
import time
import pprint

def get_Phd_info(student_dict, phd_students):
    # Playwright is used to simulate mouse clicks and screen scrolling
    # Allows us to trigger JavaScript and capture hidden HTML sections
    x_coord = 170
    y_coord = 450 #450
    for i in range(7):
        if i == 6:
            x_coord = 170
            y_coord = 570

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("https://uscinteractionlab.web.app/about/people")
            time.sleep(1)   # Allow time for page to load
            page.mouse.wheel(delta_x=0,delta_y=500) # Simulates scrolling to PhD students section
            time.sleep(0.5)   # Allow time for page to scroll
            page.mouse.click(x_coord,y_coord) # Click on coordinates which are relative to scrolling
            time.sleep(0.5)   # Allow time for student card to load
            html = page.content() # Capture page HTML
            browser.close()

        soup = BeautifulSoup(html,'html.parser')

        #print(soup.prettify())

        body_tag = soup.body.div.p
        text = body_tag.contents[0]
        #print(text)
        student_dict[phd_students[i]] = text
        x_coord += 200

phd_students = ["Leticia Pinto Alva", "Nathan Dennler", "A'di Dust", 
                "Mina Kian", "Amy O'Connell", "Zhonghao Shi",
                "Kaleen Shrestha"]

student_dict = {}
get_Phd_info(student_dict, phd_students)
pprint.pprint(student_dict)

with open("myfile.txt", 'w') as f:  
    for key, value in student_dict.items():  
        f.write('%s:%s\n' % (key, value))