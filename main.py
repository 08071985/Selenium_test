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

#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")


driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
print(driver.title)
print(driver.current_url)

time.sleep(2)


driver.find_element_by_id("search_query_top").send_keys("dress")
driver.find_element_by_name("submit_search").click()

select=Select(driver.find_element_by_id("selectProductSort"))
select.select_by_value("price:desc")
#select.select_by_index(1)
time.sleep(2)


# element = driver.find_element_by_class_name("product-container")
element = driver.find_element(by=By.CLASS_NAME, value="product-container")

actions = ActionChains(driver)
actions.move_to_element(element).perform()
time.sleep(2)
driver.find_element_by_class_name("ajax_add_to_cart_button").click()

element = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//div[@id="layer_cart"]//a[@title="Proceed to checkout"]'))
)

driver.find_element_by_xpath('//div[@id="layer_cart"]//a[@title="Proceed to checkout"]').click()

time.sleep(2)
driver.close()