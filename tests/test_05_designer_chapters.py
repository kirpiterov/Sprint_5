from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestDesignerChapters:
    def test_make_tab_buns_active_success(self, driver):
        # убедиться, что активная вкладка называется "Булки":
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TAB_ACTIVE))
        active_tab_text = driver.find_element(*TestLocators.TAB_ACTIVE).text

        assert active_tab_text == 'Булки'

    def test_make_tab_sauces_active_success(self, driver):
        # нажать на вкладку "Соусы" и убедиться, что название активной вкладки - "Соусы":
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TAB_SAUCE))
        driver.find_element(*TestLocators.TAB_SAUCE).click()
        active_tab_text = driver.find_element(*TestLocators.TAB_ACTIVE).text

        assert active_tab_text == 'Соусы'

    def test_make_tab_fillings_active_success(self, driver):
        # нажать на вкладку "Начинки" и убедиться, что название активной вкладки - "Начинки":
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TAB_FILLINGS))
        driver.find_element(*TestLocators.TAB_FILLINGS).click()
        active_tab_text = driver.find_element(*TestLocators.TAB_ACTIVE).text

        assert active_tab_text == 'Начинки'