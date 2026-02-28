import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_Keyboard:

    def test_keyboard(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.facebook.com/")
        time.sleep(2)

        actions=ActionChains(driver)

        email = driver.find_element(By.XPATH, "//input[@name='email']")

        seriesofactions = actions.move_to_element(email).key_down(Keys.SHIFT).send_keys("hello")

        seriesofactions.perform()

        # ctrl a

        actions.click(email).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

        # ctrl c

        actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

        # ctrl v into password

        password = driver.find_element(By.XPATH, "//input[@name='pass']")

        passval = actions.click(password).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL)

        passval.perform()

        driver.close()

        driver.close()