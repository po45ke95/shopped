from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

url = 'https://www.samsclub.com/p/members-mark-5-pc-led-solar-path-lights-bronze/prod26691678?xid=plp_product_1'

driver = webdriver.Chrome()
driver.get(url)

time.sleep(1000000)