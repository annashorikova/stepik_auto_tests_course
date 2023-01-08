from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ищем в тексте числа и складываем их
    num1_element = browser.find_element(By.ID, 'num1')
    num2_element = browser.find_element(By.ID, 'num2')
    num1 = num1_element.text
    num2 = num2_element.text
    y = str(int(num1) + int(num2))

    # ищем получившуюся сумму в списке
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
