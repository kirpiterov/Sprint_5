from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import generate_reg_data
from data import TestData
from locators import TestLocators


class TestRegistration:
    # тест успешной регистрации с генерацией уникальных имени-логина-пароля
    def test_registration_success(self,driver):
            # сгенерировать уникальные креды для регистрации
        name, login, password = generate_reg_data()
            # нажать кнопку "Войти в аккаунт"
        driver.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
            # нажать ссылку "Зарегистрироваться"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.LINK_REGISTER))
        driver.find_element(*TestLocators.LINK_REGISTER).click()

            # ввести полученные креды в поля
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.INPUT_NAME))
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(name)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.INPUT_EMAIL))
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(login)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.INPUT_PASSWORD))
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)

            # нажать кнопку "Зарегистрироваться"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_REGISTRATION))
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

            # ввести ту же пару логин(он же емайл) и пароль, с которыми зарегистрировались
        WebDriverWait(driver, 5).until(expected_conditions.url_matches(TestData.login_url))
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(login)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
            # нажать кнопку "Войти"
        driver.find_element(*TestLocators.BUTTON_ENTER).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

        assert driver.current_url == TestData.main_url


    # тест неуспешной регистрации при вводе валидных имени, логина и невалидного пароля
    def test_registration_fail(self,driver):
            # нажать кнопку "Войти в аккаунт"
        driver.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
            # нажать ссылку "Зарегистрироваться"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LINK_REGISTER))
        driver.find_element(*TestLocators.LINK_REGISTER).click()
            #ввести валидные имя и почту
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(TestData.user_valid_name)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(TestData.user_valid_email)
            #ввести пароль длиной 3 символа (мин. допустимо 6)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(TestData.user_not_valid_password)
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        fail_reg_text = driver.find_element(*TestLocators.TEXT_INCORRECT_PASSWORD).text

        assert fail_reg_text == 'Некорректный пароль'
