import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class Test_Suggestions:

    def test_autocomplete(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        driver.find_element(By.ID, "autocomplete").send_keys("ind")
        time.sleep(2)

        options = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item div")

        for option in options:
            if option.text == "India":
                option.click()
                break

        print("India selected successfully")

        driver.quit()