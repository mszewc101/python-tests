import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# jeśli chromedriver w PATH, można dać Service("chromedriver")
service = Service("/opt/homebrew/bin/chromedriver")  # lub inna ścieżka jeśli trzeba

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.google.com")
    time.sleep(1)
    search = driver.find_element(By.NAME, "q")
    search.send_keys("Selenium + Chrome" + Keys.RETURN)
    time.sleep(3)
    print("Tytuł strony:", driver.title)
finally:
    driver.quit()

