from selenium.webdriver.common.by import By


class TestLocators:
    BUTTON_ENTER_TO_ACCOUNT = [By.XPATH, "//button[text()='Войти в аккаунт']"]  # кнопка "Войти в аккаунт"
    BUTTON_PLACE_AN_ORDER = [By.XPATH, "//button[text()='Оформить заказ']"]  # кнопка "Оформить заказ"
    LINK_REGISTER = [By.XPATH, "//a[contains(@class,'Auth_link') and @href='/register']"]

    INPUT_NAME = [By.XPATH, "//label[contains(text(),'Имя')]/parent::div//input"]        # поле ввода Имя
    INPUT_EMAIL = [By.XPATH, "//label[contains(text(),'Email')]/parent::div//input"]     # поле ввода Email
    INPUT_PASSWORD = [By.XPATH, "//input[@type='password' and @name='Пароль']"]         # поле ввода Пароль
    BUTTON_REGISTRATION = [By.XPATH, "//button[text()='Зарегистрироваться']"]           # кнопка Зарегистрироваться

    BUTTON_ENTER = [By.XPATH, "//button[text()='Войти']"]                               # кнопка Войти
    BUTTON_EXIT = [By.XPATH, "//button[text()='Выход']"]                                # кнопка Выход

    # текст "Некорректный пароль"
    TEXT_INCORRECT_PASSWORD = [By.XPATH, "//*[text()='Некорректный пароль']"]

    # ссылка "Личный Кабинет"
    LINK_PERSONAL_ACCOUNT \
        = [By.XPATH, "//a[contains(@class,'AppHeader_header__link') and @href='/account']"]
    # ссылка Войти на форме регистрации
    LINK_ENTER \
        = [By.XPATH, "//a[contains(@class,'Auth_link') and @href='/login']"]
    # ссылка Восстановить на форме регистрации
    LINK_FORGOT_PASSWORD \
        = [By.XPATH, "//a[contains(@class,'Auth_link') and @href='/forgot-password']"]
    # ссылка Конструктор
    LINK_DESIGNER \
        = [By.XPATH, "//a[starts-with(@class,'AppHeader')]//p[text()='Конструктор']"]
    # ссылка STELLARBURGERS
    LINK_STELLARBURGERS \
        = [By.XPATH, "//div[starts-with(@class,'AppHeader_header__logo')]/a[@href='/']"]

    # активная вкладка
    TAB_ACTIVE = [By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span"]
    # вкладка Булки
    TAB_BUNS = [By.XPATH, "//span[text()='Булки']"]
    # вкладка Соусы
    TAB_SAUCE = [By.XPATH, "//span[text()='Соусы']"]
    # вкладка Начинки
    TAB_FILLINGS = [By.XPATH, "//span[text()='Начинки']"]

