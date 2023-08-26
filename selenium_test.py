from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

driver = webdriver.Firefox()
driver.get("https://www.biletix.com/etkinlik-grup/281518364/TURKIYE/tr")
raw = driver.page_source
driver.quit()
print(raw)