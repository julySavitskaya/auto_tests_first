from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

browser = webdriver.Chrome()

link =  "http://suninjuly.github.io/file_input.html"

browser.get(link)

input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Juli")
input2 = browser.find_element(By.NAME, "lastname")
input2.send_keys("Sav")
input3 = browser.find_element(By.NAME, "email")
input3.send_keys("S")

with open("file.txt", "w") as file:
    content = file.write("automationbypython")  # create file.txt file

current_dir = os.path.abspath(os.path.dirname("file.txt"))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, "file.txt")           # добавляем к этому пути имя файла 
element = browser.find_element(By.NAME, "file")
element.send_keys(file_path)


button = browser.find_element(By.CLASS_NAME, "btn-primary")
button.click()


# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла


