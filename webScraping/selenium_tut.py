from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\MinGW\chromedriver.exe"

driver = webdriver.Chrome(PATH) 

driver.get("https://smrnjeet222.github.io/")

print(driver.page_source)

driver.quit()
