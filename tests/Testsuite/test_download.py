import os.path
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

DOWNLOAD_DIR= "C://Users//ramya//Downloads"


class Test_download:

    def test_dw(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/download")
        time.sleep(2)

        alert = driver.find_element(By.XPATH, "//a[normalize-space()='alert.jpeg']")
        alert.click()
        file_path=os.path.join(DOWNLOAD_DIR, "alert.jpeg")
        assert os.path.exists(file_path)
        time.sleep(2)
        driver.close()