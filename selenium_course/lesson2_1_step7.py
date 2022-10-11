from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link =   "http://suninjuly.github.io/get_attribute.html" 

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

input = browser.find_element(By.ID, "answer")
input.send_keys(str(math.log(abs(12 * math.sin(int(x))))))

option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()

option2 = browser.find_element(By.ID, "robotsRule")
option2.click()


button = browser.find_element(By.CLASS_NAME, "btn-default")
button.click()


# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла
