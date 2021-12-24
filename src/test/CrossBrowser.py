from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browserName = 'chrome'

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.Safari()
else:
    print('please pass the correct browser name :' + browserName)

driver.implicitly_wait(5)
driver.get("https://www.gmail.com")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#identifierId').send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR, '#identifierNext').click()
time.sleep(5)

print(driver.title)
time.sleep(5)
driver.quit()
