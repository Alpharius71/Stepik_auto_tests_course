from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x и посчитать математическую функцию от x.
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # welcome_text = welcome_text_elt.text

    # Отметить checkbox "I'm the robot".
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    # Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    
    # Нажать на кнопку Submit.
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
