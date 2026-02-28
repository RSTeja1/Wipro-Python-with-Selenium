from selenium.webdriver.common.by import By

class CheckoutOverviewPage:

    overview_title = (By.XPATH, "//span[text()='Checkout: Overview']")
    total = (By.XPATH, "//div[@class='summary_total_label']")
    finish_btn = (By.XPATH, "//button[@id='finish']")

    def __init__(self, driver):
        self.driver = driver

    def is_overview_page_loaded(self):
        return self.driver.find_element(*self.overview_title).is_displayed()

    def get_total_price(self):
        return self.driver.find_element(*self.total).text

    def click_finish(self):
        self.driver.find_element(*self.finish_btn).click()