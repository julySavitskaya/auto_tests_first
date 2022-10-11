from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

link =  "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

def sum(x, y):
  return str(x + y)

x_element = browser.find_element(By.ID, "num1" )
y_element = browser.find_element(By.ID, "num2" ) 
x = int(x_element.text)
y = int(y_element.text)
z = str(int(x_element.text)+int(y_element.text))
print(z)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(value=str(z))


button = browser.find_element(By.CLASS_NAME, "btn-default")
button.click()


# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла
