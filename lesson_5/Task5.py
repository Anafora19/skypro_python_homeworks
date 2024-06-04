#Поле ввода

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()
chrome = webdriver.Chrome()

#Откройте страницу http://the-internet.herokuapp.com/inputs.

try:
    firefox.get("http://the-internet.herokuapp.com/inputs")
    chrome.get("http://the-internet.herokuapp.com/inputs")
#Введите в поле текст 1000
    input_field = firefox.find_element(By.TAG_NAME, "input")
    input_field1 = chrome.find_element(By.TAG_NAME, "input")
    input_field.send_keys("1000")
    sleep(2)
#Очистите это поле (метод clear)
    input_field.clear()
    input_field1.clear()
    sleep(1)
#Введите в это же поле текст 999
    input_field.send_keys("999")
    input_field1.send_keys("999")
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
    chrome.quit()


