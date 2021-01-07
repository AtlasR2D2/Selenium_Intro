from selenium import webdriver
import time
from dateutil.parser import parse

# ---------------------------------------------------------------------------------------------
# ------------------------------------ ITEM: 24kg Kettlebell ----------------------------------
Amazon_URL = "https://www.amazon.co.uk/dp/B00BACJTTU/ref=twister_B00KRHXN6Y?_encoding=UTF8&psc=1"
# ---------------------------------------------------------------------------------------------
#

chrome_driver_path = r'C:\Users\micha\Documents\Programming\Web Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get(Amazon_URL)

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

driver.get("https://www.python.org/")

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# about_link = driver.find_element_by_xpath("//*[@id='container']/li[1]/a")
# print(about_link.text)


def is_date(value, fuzzy=False):
    """Will check whether a string value can be cast as a date"""
    try:
        parse(value, fuzzy=fuzzy)
        return True
    except ValueError:
        return False

# Bulk Text Method
upcoming_events = driver.find_element_by_css_selector(".event-widget ul").text
key_count = 0
upcoming_events_dict = {}
for line in iter(upcoming_events.splitlines()):
    if is_date(line):
        date_x = line
    else:
        name_x = line
        upcoming_events_dict[key_count] = {"date": date_x, "name": name_x}
        key_count += 1

print("Version 1: Bulk Text")
print(upcoming_events_dict)

# More Elegant Method
driver.get("https://www.python.org/")
upcoming_events = driver.find_elements_by_css_selector(".event-widget li")
key_count = 0
upcoming_events_dict = {}
key_count = 0
for event in upcoming_events:
    date_x = event.find_element_by_css_selector("time").text
    name_x = event.find_element_by_css_selector("a").text
    upcoming_events_dict[key_count] = {"date": date_x, "name": name_x}
    key_count += 1

print("Version 2: More Elegant Method")
print(upcoming_events_dict)

# time.sleep(2)

# driver.close()    # Close Active Tab
driver.quit()   # Close Session