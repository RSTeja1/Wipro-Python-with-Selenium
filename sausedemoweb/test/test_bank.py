import time
from Pages.login_bank import LoginPage
from Pages.manager_login import ManagerPage
from Pages.customer_login import CustomerPage

def test_complete_banking_flow(driver):

    home = LoginPage(driver)
    manager = ManagerPage(driver)
    customer = CustomerPage(driver)

    # Open Application
    home.open()
    time.sleep(2)

    # Bank Manager Login
    home.click_bank_manager_login()
    time.sleep(2)

    # Add Customer
    manager.add_customer("Surya", "Teja", "63712")
    time.sleep(2)

    # Open Account
    manager.open_account("Surya Teja", "Dollar")
    time.sleep(2)

    # Customer Login
    home.open()
    home.click_customer_login()
    time.sleep(2)

    customer.login("Surya Teja")
    time.sleep(2)

    # Deposit
    customer.deposit("100")
    time.sleep(2)

    # Withdraw
    customer.withdraw("40")
    time.sleep(2)

    # Validate Balance
    balance = customer.get_balance()
    assert balance == "60"