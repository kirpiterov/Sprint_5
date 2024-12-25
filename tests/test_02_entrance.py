from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import TestData
from locators import TestLocators

class TestEntrance:
    def test_entrance_main_success(self,driver):
        #войти в аккаунт и авторизоваться:
        driver.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(TestData.user_valid_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(TestData.user_valid_password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        #войти в ЛК и проверить логин:
        driver.find_element(*TestLocators.LINK_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.INPUT_NAME))
        user_name = driver.find_element(*TestLocators.INPUT_NAME).get_attribute('value')

        assert user_name == TestData.user_valid_name

    def test_entrance_from_pers_account_success(self,driver):
        # войти в ЛК и авторизоваться:
        driver.find_element(*TestLocators.LINK_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.INPUT_EMAIL))
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(TestData.user_valid_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(TestData.user_valid_password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        #вернуться в ЛК и проверить логин:
        driver.find_element(*TestLocators.LINK_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.INPUT_NAME))
        user_name = driver.find_element(*TestLocators.INPUT_NAME).get_attribute('value')

        assert user_name == TestData.user_valid_name

    def test_entrance_from_reg_form_link_success(self,driver):
        # нажать Войти в аккаунт, кликнуть ссылку Зарегистрироваться, кликнуть ссылку Войти
        driver.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_REGISTER).click()
        driver.find_element(*TestLocators.LINK_ENTER).click()
        # авторизоваться
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(TestData.user_valid_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(TestData.user_valid_password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        #войти в ЛК и проверить логин:
        driver.find_element(*TestLocators.LINK_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.INPUT_NAME))
        user_name = driver.find_element(*TestLocators.INPUT_NAME).get_attribute('value')

        assert user_name == TestData.user_valid_name

    def test_entrance_from_forgot_password_form_success(self,driver):
        # нажать Войти в аккаунт, кликнуть ссылку Восстановить пароль, кликнуть ссылку Войти
        driver.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_FORGOT_PASSWORD).click()
        driver.find_element(*TestLocators.LINK_ENTER).click()
        # авторизоваться
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(TestData.user_valid_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(TestData.user_valid_password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        #войти в ЛК и проверить логин:
        driver.find_element(*TestLocators.LINK_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.INPUT_NAME))
        user_name = driver.find_element(*TestLocators.INPUT_NAME).get_attribute('value')

        assert user_name == TestData.user_valid_name