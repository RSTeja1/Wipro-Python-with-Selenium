from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://rsuitejs.com/components/date-picker/")
time.sleep(3)
driver.execute_script("window.scrollBy(0,-1000)")
# Open Date Picker
driver.find_element(By.XPATH, "//input[@id='rs-:r2b:']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//span[normalize-space()='24']").click()
time.sleep(1)

# Click OK
driver.find_element(By.XPATH, "//button[normalize-space()='OK']").click()
time.sleep(2)
driver.quit()
