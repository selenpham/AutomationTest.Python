from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb
import time

# driver =webdriver.Chrome()
# driver.get("http://demostore.supersqa.com")

# cart = driver.find_element(By.ID, "site-header-cart")
# cart.click()

# driver.get("http://demostore.supersqa.com/my-account/")
# u_name = driver.find_element(By.ID, "username")
# u_name.send_keys("myusername")
# pdb.set_trace()

driver =webdriver.Chrome()

driver.get("http://demostore.supersqa.com")
cart = driver.find_element(By.CSS_SELECTOR, ".nav-menu > .page-item-7.page_item > a")
time.sleep(10)
cart.click()


myaccount = driver.find_element(By.CSS_SELECTOR, ".nav-menu > .page-item-9.page_item > a")
time.sleep(10)
myaccount.click();