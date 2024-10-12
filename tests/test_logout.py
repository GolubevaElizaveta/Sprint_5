from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.locators import TestLocators
from conftest import driver, login


class TestLogout:
    # Проверка выхода из личного кабинета
    def test_logout_of_personal_account_success(self, driver, login):
        self.wait_for_order_button(driver)
        self.navigate_to_personal_account(driver)
        self.logout(driver)
        self.verify_logout(driver)

    def wait_for_order_button(self, driver):
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))

    def navigate_to_personal_account(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.profile))

    def logout(self, driver):
        driver.find_element(*TestLocators.button_logout).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.button_login))

    def verify_logout(self, driver):
        assert driver.find_element(*TestLocators.button_login).is_displayed(), \
            "Кнопка 'Войти' не отображается после выхода."