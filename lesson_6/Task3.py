#Дождаться картинки

#Перейдите на сайт: https://bonigarcia.dev/selenium-webdriver-java/loading-images.html. #Дождитесь загрузки всех картинок.
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
waiting = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'text'), 'Done!'))

#Получите значение атрибута src у 3-й картинки. 
get_value = driver.find_element(By.ID, "award").get_attribute("src")

#Выведите значение в консоль.
print(get_value)
driver.quit()
