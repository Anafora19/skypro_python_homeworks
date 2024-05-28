#Клик по кнопке

#Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")

#Пять раз кликните на кнопку Add Element

for _ in range(5):
    add_button = chrome.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()
    add_button = firefox.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()
    sleep(1)

#Соберите со страницы список кнопок Delete

chrome_delete_buttons = chrome.find_element(
      "xpath", '//button[text()="Delete"]')
firefox_delete_buttons = firefox.find_elements(
      "xpath", '//button[text()="Delete"]')

#Выведите на экран размер списка.

print(f"Размер списка кнопок Delete в Chrome: {len(chrome_delete_buttons)}")
print(f"Размер списка кнопок Delete в Firefox: {len(firefox_delete_buttons)}")
