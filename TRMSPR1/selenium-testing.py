from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver = webdriver.Chrome("C:/Users/tsagb/Documents/RevatureWork/chromedriver.exe")

driver.get("https://www.google.com/")