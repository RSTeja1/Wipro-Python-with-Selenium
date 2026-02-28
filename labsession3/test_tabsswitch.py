import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


class Test_TabSwitch:

    def test_tab_switch(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        parent = driver.current_window_handle

        # Click open tab button
        driver.find_element(By.ID, "opentab").click()

        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: len(d.window_handles) > 1)

        # Switch to new tab
        for tab in driver.window_handles:
            if tab != parent:
                driver.switch_to.window(tab)
                break

        print("Child Tab Title:", driver.title)

        # Assertion
        assert "QAClick Academy" in driver.title

        driver.close()

        # Switch back to parent tab
        driver.switch_to.window(parent)
        print("Parent Tab Title:", driver.title)

        driver.quit()