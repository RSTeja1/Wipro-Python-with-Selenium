from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_iframe_all_text():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    # scroll to iframe
    driver.execute_script("window.scrollBy(0,1000);")

    # switch to iframe
    driver.switch_to.frame("courses-iframe")

    wait = WebDriverWait(driver, 15)

    # wait until body loads
    body = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # get all visible text inside iframe
    all_text = body.text

    print("\n========= IFRAME FULL TEXT =========\n")
    print(all_text)

    # validation example
    assert "Selenium" in all_text

    # back to main page
    driver.switch_to.default_content()
    driver.quit()