#Форма авторизации

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()
chrome = webdriver.Chrome()

#Откройте страницу http://the-internet.herokuapp.com/login.
try:
    firefox.get("http://the-internet.herokuapp.com/login")
    chrome.get("http://the-internet.herokuapp.com/login")

#В поле username введите значение tomsmith
    input_name = firefox.find_element(By.ID, "username").send_keys("tomsmith")
    input_name1 = chrome.find_element(By.ID, "username").send_keys("tomsmith")

#В поле password введите значение SuperSecretPassword!
    input_pass = firefox.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    input_pass1 = chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
#Нажмите кнопку Login
    button = firefox.find_element(By.TAG_NAME, "button").click()
    button1 = chrome.find_element(By.TAG_NAME, "button").click()
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
    chrome.quit()
