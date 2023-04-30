from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

#オプションの設定
options = webdriver.ChromeOptions() 
options.add_argument('--disable-extensions')
options.add_argument('--ignore-certificate-errors')


driver = webdriver.Chrome(options = options)
driver.get('https://www.netkeiba.com/')
time.sleep(5)

pickuprace = driver.find_element(By.XPATH, "//*[@id='top_race_main']/section/section/div[2]/ul/li[1]/a").get_attribute("href")
print(pickuprace)

driver.quit() 