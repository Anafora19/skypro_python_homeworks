
#клик по кнопке с css-классом

#откройте страницу http://uitestingplayground.com/classattr.
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()
chrome = webdriver.Chrome()

#кликните на синюю кнопку. запустите скрипт три раза подряд. убедитесь, что он отработает одинаково.
#кнопка - <button class="btn btn-primary" type="button" id="f53abb4c-3d74-434b-4260-60d2d1d2dd06">button with dynamic id</button>
try:
    count = 0
    firefox.get("http://uitestingplayground.com/dynamicid")
    chrome.get("http://uitestingplayground.com/dynamicid")

    for _ in range(3):
        blue_button = firefox.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
        blue_button = chrome.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
        count += 1
        print(count)
        firefox.refresh()
        chrome.refresh()

    print("final count:", count)
    sleep(1)

except Exception as ex:
    print(ex)

finally:
    firefox.quit()
    chrome.quit()
