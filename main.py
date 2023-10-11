from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import re
import random

url = 'https://www.samsclub.com/p/members-mark-5-pc-led-solar-path-lights-bronze/prod26691678?xid=plp_product_1'

driver = webdriver.Chrome()
driver.get(url)

time.sleep(20)

def click_element_if_exists(xpath1, xpath2):
    element = None
    attempts = random.randint(3,5)
    for _ in range(attempts):
        try:
            element = driver.find_element(By.XPATH, xpath1)
            break
        except:
            pass

        try:
            element = driver.find_element(By.XPATH, xpath2)
            break
        except:
            pass

    if element is None:
        return False

    actions = ActionChains(driver)
    actions.click_and_hold(element).perform()
    time.sleep(10)
    actions.release(element).perform()
    
    return True

# Try to find and click the element using two possible XPaths
if click_element_if_exists('//*[@id="px-captcha"]', '//*[@id="FKlJURsmohuOGYu"]') == True:

    try:
        # Get the title
        title = driver.title
        if " - Sam's Club" in title:
            title = title.split(" - Sam's Club")[0]

        # Get the desired data
        desired_element = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/div/div[4]/div[2]/div[3]/div')
        desired_data = desired_element.text

        # Extract the price from the desired data
        price_match = re.search(r'\$(\d+\.\d+)', desired_data)
        if price_match:
            price = price_match.group(1) + ' USD'
        else:
            price = "Price not found"

        print("Title:", title)
        print("Price:", price)
    except Exception as e:
        print(f"Error occurred: {e}")

else:
    print('function error')

# Close the driver
driver.quit()
