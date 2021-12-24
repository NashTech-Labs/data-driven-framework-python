import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://www.facebook.com/')
driver.maximize_window()


userName = driver.find_element(By.ID, 'email')
passWord = driver.find_element(By.ID, 'pass')
button = driver.find_element(By.NAME, 'login')

workbook = xlrd.open_workbook("TestData.xlsx")
sheet = workbook.sheet_by_name("login")

# get total number of rows:
rowCount = sheet.nrows
colCount = sheet.ncols
print(rowCount)
print(colCount)

for curr_row in range(1, rowCount):
    user_name = sheet.cell_value(curr_row, 0)
    pass_word = sheet.cell_value(curr_row, 1)
    print(user_name, pass_word)

    userName.clear()
    userName.send_keys(user_name)
    passWord.clear()
    passWord.send_keys(pass_word)
    #button.click()
    time.sleep(1000)


