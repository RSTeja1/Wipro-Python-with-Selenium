import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class Test_Waits:

    def test_waits(self):

        # Chrome options to avoid automation detection
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        driver.maximize_window()
        driver.get("https://www.facebook.com/")

        wait = WebDriverWait(driver, 20)

        # Wait for email field
        email_box = wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_box.send_keys("test@gmail.com")

        # Wait for password field
        password_box = wait.until(
            EC.presence_of_element_located((By.NAME, "pass"))
        )
        password_box.send_keys("Test123")

        print("Elements located successfully")

        driver.quit()