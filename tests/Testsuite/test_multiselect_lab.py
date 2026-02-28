import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    name = driver.find_element(By.NAME, "username")
    name.send_keys("Admin")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("admin123")
    time.sleep(2)

    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_btn.click()
    time.sleep(5)

    pim = driver.find_element(By.XPATH, "//span[text()='PIM']")
    pim.click()
    time.sleep(2)

    checkboxes = driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']//span")
    for i in range(1, len(checkboxes)):
        checkboxes[i].click()
        time.sleep(1)

    (driver.close())

