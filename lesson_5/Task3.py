#Клик по кнопке с CSS-классом

#Откройте страницу http://uitestingplayground.com/classattr.
from selenium import webdriver
from time import sleep

firefox = webdriver.Firefox()
chrome = webdriver.Chrome()

#Кликните на синюю кнопку.Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
#Кнопка - <button class="btn btn-primary" type="button" id="f53abb4c-3d74-434b-4260-60d2d1d2dd06">Button with Dynamic ID</button>
try:
    count = 0
    firefox.get("http://uitestingplayground.com/dynamicid")
    chrome.get("http://uitestingplayground.com/dynamicid")

    for _ in range(3):
        blue_button = firefox.find_element_by_xpath("//button[contains(@class, 'btn btn-primary')]").click()
        blue_button = chrome.find_element("xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn btn-primary ')]").click()
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
