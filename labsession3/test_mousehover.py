from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_mouse_hover_top():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    # scroll to mouse hover section
    driver.execute_script("window.scrollBy(0,600);")

    wait = WebDriverWait(driver, 10)

    # locate hover button
    hover_button = wait.until(EC.visibility_of_element_located((By.ID, "mousehover")))

    # perform hover
    actions = ActionChains(driver)
    actions.move_to_element(hover_button).perform()

    # click TOP (appears after hover)
    top_option = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Top")))
    top_option.click()

    # validate page scrolled to top
    url = driver.current_url
    print("Current URL:", url)

    assert "AutomationPractice" in url

    driver.quit()