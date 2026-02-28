import os.path
import time
from itertools import count

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()
time.sleep(2)

title = driver.title
print(title)
url = driver.current_url
print(url)
time.sleep(2)
driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)
driver.refresh()

driver.close()