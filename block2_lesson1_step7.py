from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x и посчитать математическую функцию от x.
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

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

# не забываем оставить пустую строку в конце файла
