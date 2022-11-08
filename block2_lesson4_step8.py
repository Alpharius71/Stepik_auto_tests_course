from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # browser.maximize_window()
    # browser.implicitly_wait(5)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    button = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(
        (By.ID, "price"), "100")
    )
    button.click()
    
    # Нажать на кнопку "Book"
##    button = browser.find_element(By.ID, "book")
##    button.click()

    # Ваш код, который заполняет обязательные поля
##    input1 = browser.find_element(By.NAME, "firstname")
##    input1.send_keys("Ivan")
##    input2 = browser.find_element(By.NAME, "lastname")
##    input2.send_keys("Petrov")
##    input3 = browser.find_element(By.NAME, "email")
##    input3.send_keys("email@email.com")

    # Здесь загружаем файл
##    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
##    file_path = os.path.join(current_dir, 'Test.txt')    # добавляем к этому пути имя файла 
##    element = browser.find_element(By.ID, "file")
##    element.send_keys(file_path)

    # Принять confirm
##    confirm = browser.switch_to.alert
##    confirm.accept()

    # Переключиться на новую вкладку
##    new_window = browser.window_handles[1]
##    browser.switch_to.window(new_window)
##
    # Считать значение для переменной x и посчитать математическую функцию от x.
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
##
    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)    
##    
    # Отправляем заполненную форму
    button = browser.find_element(By.ID, "solve")
    button.click()
##
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
##    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
