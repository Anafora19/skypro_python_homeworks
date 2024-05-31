#Клик по кнопке без ID

#Откройте страницу http://uitestingplayground.com/dynamicid.
from selenium import webdriver
from time import sleep

firefox = webdriver.Firefox()
chrome = webdriver.Chrome()
#Кликните на синюю кнопку. Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.

try:
    count = 0
    firefox.get("http://uitestingplayground.com/dynamicid")
    chrome.get("http://uitestingplayground.com/dynamicid")

    for _ in range(3):
        blue_button = firefox.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()
        blue_button1 = chrome.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()
        count += 1
        print(count)
        firefox.refresh()
        chrome.refresh()

    print("Final count:", count)
    sleep(1)

except Exception as ex:
    print(ex)

finally:
    firefox.quit()
    chrome.quit()