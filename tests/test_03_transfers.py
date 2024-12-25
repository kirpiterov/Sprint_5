from data import TestData
from locators import TestLocators

class TestTransfers:
    #переход по ссылке в Личный кабинет
    def test_transfer_to_pers_account(self,driver):
        driver.find_element(*TestLocators.LINK_PERSONAL_ACCOUNT).click()
        assert driver.current_url == TestData.login_url

    # переход по ссылке в Личный кабинет, затем в Конструктор
    def test_transfer_from_pers_account_to_designer(self,driver):
        driver.find_element(*TestLocators.LINK_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_DESIGNER).click()
        assert driver.current_url == TestData.main_url

    # переход по ссылке в Личный кабинет, затем на логотип Stellar Burgers
    def test_transfer_from_pers_account_to_stellarburger(self,driver):
        driver.find_element(*TestLocators.LINK_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_STELLARBURGERS).click()
        assert driver.current_url == TestData.main_url