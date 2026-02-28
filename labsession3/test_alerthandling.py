import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_AlertHandling:

    def test_alert(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        driver.find_element(By.ID, "name").send_keys("Ramya")
        driver.find_element(By.ID, "alertbtn").click()

        wait = WebDriverWait(driver, 10)
        alert = wait.until(EC.alert_is_present())

        print("Alert Text:", alert.text)

        # Assertion
        assert "Maneesha" in alert.text

        alert.accept()

        driver.quit()