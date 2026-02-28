from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_fixed_header_scroll_chennai():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    # 🔹 Scroll main page down to Fixed Header section
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(2)

    # 🔹 Scroll inside fixed header table
    scroll_table = driver.find_element(By.CSS_SELECTOR, ".tableFixHead")
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_table)
    time.sleep(2)

    # 🔹 Get all city cells (3rd column)
    cities = driver.find_elements(By.XPATH, "//div[@class='tableFixHead']//td[3]")

    found = False

    for city in cities:
        if city.text.strip().lower() == "chennai":
            print("Chennai Found")
            found = True
            break

    assert found, "Chennai not found in fixed header table"

    driver.quit()