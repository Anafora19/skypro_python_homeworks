#Нажать на кнопку

#Перейдите на страницу http://uitestingplayground.com/ajax.
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://uitestingplayground.com/ajax")

add_button = driver.find_element(By.XPATH, '//button[text()="Button Triggering AJAX Request"]').click() #Нажмите на синюю кнопку

#Получите текст из зеленой плашки.
green_box = WebDriverWait(driver, 40, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.bg-success'))).text
txt = green_box

#Выведите его в консоль (Data loaded with AJAX get request).
print(txt)
driver.quit()