from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r'chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)


sign_up_form_link = "http://secure-retreat-92358.herokuapp.com/"

driver.get(sign_up_form_link)

first_name = input("Enter your first name: ").title()
last_name = input("Enter your first name: ").title()
email = input("Enter your first name: ")

input_fields = {"fName": first_name, "lName": last_name, "email": email}

for field_key in input_fields.keys():
    field_input = input_fields[field_key]
    field_x = driver.find_element_by_name(field_key)
    field_x.send_keys(field_input)

sign_up_button = driver.find_element_by_xpath(r"/html/body/form/button")
sign_up_button.click()

time.sleep(2)

# driver.close()    # Close Active Tab
driver.quit()   # Close Session