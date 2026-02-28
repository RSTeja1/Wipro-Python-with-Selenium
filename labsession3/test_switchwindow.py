import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


class Test_SwitchWindow:

    def test_window_switch(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        parent = driver.current_window_handle

        # Click open window
        driver.find_element(By.ID, "openwindow").click()

        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: len(d.window_handles) > 1)

        # Switch to child window
        for window in driver.window_handles:
            if window != parent:
                driver.switch_to.window(window)
                break

        print("Child Window Title:", driver.title)

        # ✅ Correct assertion
        assert "QAClick Academy" in driver.title

        driver.close()

        # Switch back to parent window
        driver.switch_to.window(parent)
        print("Parent Window Title:", driver.title)

        driver.quit()
