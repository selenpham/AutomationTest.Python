from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome()

driver.get("http://demostore.supersqa.com")

product = driver.find_element(By.CLASS_NAME, "product")
products = driver.find_elements(By.CLASS_NAME, "product")
print(product)
print("+++++++++++++++++++")
print(products)