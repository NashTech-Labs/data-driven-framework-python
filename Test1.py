import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="//usr/local/share/chromedriver")
driver.implicitly_wait(5)
driver.get("https://www.google.co.in/")
driver.maximize_window()

print(driver.title)
driver.find_element(By.NAME, 'q').send_keys("youtube")

time.sleep(5)

optionsList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')

print(len(optionsList))

for ele in optionsList:
    print(ele.text)
    if ele.text == 'youtube music':
        ele.click()
        break
        time.sleep(5)
driver.quit()
