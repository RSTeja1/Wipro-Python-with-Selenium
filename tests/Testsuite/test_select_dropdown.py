import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_all_elements():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://trytestingthis.netlify.app")
    driver.maximize_window()
    time.sleep(2)

    # -------------------------
    # Textbox
    # -------------------------
    name_box = driver.find_element(By.ID, "fname")
    name_box.clear()
    name_box.send_keys("Maneesha")
    print("Entered Name:", name_box.get_attribute("value"))

    # -------------------------
    # Radio Button (Cannot Deselect Directly)
    # -------------------------
    male_radio = driver.find_element(By.ID, "male")
    driver.execute_script("arguments[0].scrollIntoView();", male_radio)
    male_radio.click()

    print("Male Selected:", male_radio.is_selected())

    # To change selection, select another radio (if available)
    female_radio = driver.find_element(By.ID, "female")
    female_radio.click()

    print("Female Selected:", female_radio.is_selected())

    # -------------------------
    # Checkbox (Can Deselect)
    # -------------------------
    checkbox = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]")
    checkbox.click()
    print("Checkbox Selected:", checkbox.is_selected())

    time.sleep(2)

    # Deselect checkbox
    if checkbox.is_selected():
        checkbox.click()

    print("Checkbox After Deselect:", checkbox.is_selected())

    # -------------------------
    # Get Heading Text
    # -------------------------
    heading = driver.find_element(By.TAG_NAME, "h1").text
    print("Heading Text:", heading)

    time.sleep(2)
    driver.quit()