import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_Keyboard:

    def test_keyboard(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/upload")
        time.sleep(2)

        browse = driver.find_element(By.XPATH, "//input[@id='file-upload']")
        browse.send_keys("C:/Users/ramya/Downloads/degree certificate ramya.pdf")
        time.sleep(2)
        upload=driver.find_element(By.XPATH, "//input[@id='file-submit']")
        upload.click()
        time.sleep(2)
        fileupload= driver.find_element(By.XPATH, "//h3[normalize-space()='File Uploaded!']")
        time.sleep(2)
        assert fileupload.text == "File Uploaded!"
        driver.close()