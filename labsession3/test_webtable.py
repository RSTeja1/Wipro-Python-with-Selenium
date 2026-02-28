from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


def test_webtable():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    rows = driver.find_elements(By.XPATH, "//td[contains(text(),'Advanced Selenium Framework Pageobject, TestNG, Ma')]")

    found = False

    for row in rows:
        if "Advanced Selenium Framework Pageobject, TestNG, Maven, Jenkins,C" in row.text:
            print("Course Found:", row.text)
            found = True
            break

    assert found

    driver.quit()