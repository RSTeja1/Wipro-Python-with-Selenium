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
class Test_frame:
    def test_frame(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/tables")

        rows = driver.find_elements(By.XPATH, "//table[@id = 'table1']/tbody/tr")
        for i in rows:
            print(i.text)
        time.sleep(2)

        cols = driver.find_elements(By.XPATH, "//table[@id = 'table1']/tbody/tr[1]/td")
        for i in cols:
            print(i.text)
        time.sleep(2)
        celldata = driver.find_element(By.XPATH, "//table[@id = 'table1']/tbody/tr[3]/td[4]")
        assert "$100.00" in celldata.text

        driver.quit()