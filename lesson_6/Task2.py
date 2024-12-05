#Переименовать кнопку

#Перейдите на сайт: http://uitestingplayground.com/textinput.
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://uitestingplayground.com/textinput")

#Укажите в поле ввода текст SkyPro.
element = driver.find_element(By.ID, 'newButtonName').send_keys("SkyPro") #<input class="form-control" type="text" placeholder="MyButton" id="newButtonName">

#Нажмите на синюю кнопку.
add_button = driver.find_element(By.ID, 'updatingButton').click()

#Получите текст кнопки и выведите в консоль (SkyPro).
text_button = driver.find_element(By.ID, 'updatingButton').text
print(text_button)
driver.quit()

