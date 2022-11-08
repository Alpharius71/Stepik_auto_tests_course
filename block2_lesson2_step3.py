from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменных x и y и посчитать математическую сумму.
    num1 = browser.find_element(By.ID, "num1")
    first_num = num1.text

    num2 = browser.find_element(By.ID, "num2")
    second_num = num2.text
    
    full_num =  int(first_num) + int(second_num)

    # ищем элемент с текстом
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(full_num)) 
    
    # Нажать на кнопку Submit.
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
