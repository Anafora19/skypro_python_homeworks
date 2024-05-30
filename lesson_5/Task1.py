#Клик по кнопке

#Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")

# пять раз кликните на кнопку add element
for _ in range(5):
    add_button = chrome.find_element(By.XPATH, '//button[text()="Add Element"]').click()
    add_button = firefox.find_element(By.XPATH, '//button[text()="Add Element"]').click()
    sleep(1)

# соберите со страницы список кнопок delete
chrome_delete_buttons = chrome.find_elements(By.XPATH, '//button[text()="Delete"]')
firefox_delete_buttons = firefox.find_elements(By.XPATH, '//button[text()="Delete"]')

# выведите на экран размер списка
print(f"размер списка кнопок delete в chrome: {len(chrome_delete_buttons)}")
print(f"размер списка кнопок delete в firefox: {len(firefox_delete_buttons)}")