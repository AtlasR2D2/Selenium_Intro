from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r'chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

wikipedia_page = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(wikipedia_page)
#
# total_article_count = driver.find_element_by_xpath("//*[@id=\"articlecount\"]/a[1]")
# total_article_count.click()

# driver.get(wikipedia_page)

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

time.sleep(2)

# driver.close()    # Close Active Tab
driver.quit()   # Close Session