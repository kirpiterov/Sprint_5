from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import TestData
from locators import TestLocators

class TestExit:
    def test_exit_from_pers_account(self,driver):
            #войти в ЛК и авторизоваться:
        driver.find_element(*TestLocators.LINK_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.INPUT_EMAIL))

        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(TestData.user_valid_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(TestData.user_valid_password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
            #вернуться в ЛК и нажать Выход:
        driver.find_element(*TestLocators.LINK_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_EXIT))
        driver.find_element(*TestLocators.BUTTON_EXIT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ENTER))
            #убедиться, что мы на странице логина:
        assert driver.current_url == TestData.login_url