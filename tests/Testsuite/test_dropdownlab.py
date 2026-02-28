import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def test_dropdown():

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get("https://trytestingthis.netlify.app")
    time.sleep(2)

    # -----------------------------
    # First dropdown (Single Select)
    # -----------------------------
    single = Select(driver.find_element(By.ID, "option"))
    single.select_by_visible_text("Option 2")
    time.sleep(2)

    # -----------------------------
    # Second dropdown (Multi Select)
    # -----------------------------
    multi = Select(driver.find_element(By.ID, "owc"))

    # Select options
    multi.select_by_visible_text("Option 1")
    multi.select_by_visible_text("Option 3")
    time.sleep(2)

    # -----------------------------
    # Deselect options
    # -----------------------------

    # Deselect by visible text
    multi.deselect_by_visible_text("Option 1")
    time.sleep(2)

    # Deselect by index
    multi.deselect_by_index(2)
    time.sleep(2)

    # Select again for demo
    multi.select_by_visible_text("Option 2")
    multi.select_by_visible_text("Option 3")
    time.sleep(2)

    # Deselect all
    multi.deselect_all()
    time.sleep(2)

    driver.quit()