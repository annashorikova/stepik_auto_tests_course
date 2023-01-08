from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'input_value')
    x = int(x_element.text)
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    button.click()

finally:
    time.sleep(5)
    browser.quit()