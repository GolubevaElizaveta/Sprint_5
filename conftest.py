import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.locators import TestLocators
from src.data import UsersTestData

# Фикстура веб-драйвера
@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации веб-драйвера Chrome."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")  # Замените нужным URL
    yield driver
    driver.quit()

# Фикстура для авторизации с валидной парой логин/пароль перед тестами
@pytest.fixture
def login(driver):
    """Фикстура для авторизации пользователя с использованием заранее определённых логина и пароля."""
    driver.find_element(*TestLocators.button_login_in_main).click()
    driver.find_element(*TestLocators.input_email_auth).send_keys(UsersTestData.email)
    driver.find_element(*TestLocators.input_password_auth).send_keys(UsersTestData.password)
    driver.find_element(*TestLocators.button_login).click()