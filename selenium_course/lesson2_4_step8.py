from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100"))

button1 = browser.find_element(By.ID, "book")
button1.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value" )
x = x_element.text
y = calc(x)

input = browser.find_element(By.ID, "answer")
input.send_keys(str(math.log(abs(12 * math.sin(int(x))))))


button2 = browser.find_element(By.ID, "solve")
button2.click()

time.sleep(30)

browser.quit()

# не забываем оставить пустую строку в конце файла
