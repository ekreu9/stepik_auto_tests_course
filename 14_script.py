from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100" )
        )
    button = browser.find_element(By.ID, "book")
    button.click()

    input1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = input1.text
    y = calc(x)
    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input2.send_keys(y)
    
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла

