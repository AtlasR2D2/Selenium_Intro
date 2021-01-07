from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

GAIN_REWARD_INCREMENT = 5       # Gain a reward every X seconds

cookie_url = "http://orteil.dashnet.org/experiments/cookie/"

chrome_driver_path = r'chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(cookie_url)

# Cookie Clicker Loop
time_elapsed = 0
time_start = time.time()
current_time = time_start


def increment_time():
    return round(time.time() - time_start,0)


def define_cookie():
    return driver.find_element_by_id("cookie")


def click_cookie(cookie_x):
    cookie_x.click()


def getClick_Count():
    return int(driver.find_element_by_id("money").text)


def get_best_reward(money_x, rewards_x):
    best_reward_amount = 0
    best_reward = ""
    for reward in rewards_x:
        cookie_cost = int(reward.find_element_by_css_selector("b").text.split("-")[1].strip())
        if cookie_cost <= money_x:
            if cookie_cost > best_reward_amount:
                best_reward_amount = cookie_cost
                best_reward = reward.get_attribute("id")
    # Claim reward
    if len(best_reward) != 0:
        for reward in rewards_x:
            if reward.get_attribute("id") == best_reward:
                reward.click()
                break

# Define cookie so you don't redefine it all the time
cookie = define_cookie()

blnCheckAvailable = True # So you only check once every 5 seconds not 100 times!
while True:
    current_time = increment_time()
    if current_time % GAIN_REWARD_INCREMENT == 0 and blnCheckAvailable:
        # Check Rewards
        money = getClick_Count()
        rightPanel = driver.find_element_by_id("rightPanel")
        rewards = rightPanel.find_elements_by_xpath("//*[contains(@id,'buy')]")
        available_rewards = [reward for reward in rewards if reward.get_attribute("class") != "grayed"]
        get_best_reward(money, available_rewards)
        blnCheckAvailable = False   # So you only check once every 5 seconds not 100 times!
    else:
        if current_time % GAIN_REWARD_INCREMENT != 0:
            blnCheckAvailable = True
        # What you waiting for click that cookie!
        click_cookie(cookie)

driver.quit()   # Close Session

