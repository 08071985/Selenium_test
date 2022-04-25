import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.binary_location = r'C:\Users\siwar.bouhamed\AppData\Local\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(executable_path="D:\\geckodriver.exe", options=options)

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")


driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)

time.sleep(2)
# driver.find_element_by_name("name").send_keys("Siwar")
driver.find_element_by_css_selector("input[name='name']").send_keys("Siwar")
time.sleep(2)

driver.find_element_by_name("email").send_keys("siwar.bouhamed@gmail.com")

time.sleep(2)
driver.find_element_by_id("exampleInputPassword1").send_keys("azerty")

time.sleep(2)
driver.find_element_by_id("exampleCheck1").click()
time.sleep(2)
driver.find_element_by_id("exampleFormControlSelect1").click()
time.sleep(2)
driver.find_element_by_id("inlineRadio2").click()
time.sleep(2)
driver.find_element(by=By.NAME, value="bday").send_keys("08/07/1985")
time.sleep(2)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(2)

driver.close()