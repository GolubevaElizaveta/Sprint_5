from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.locators import TestLocators
from conftest import driver, login


class TestNavigateToConstructor:
    # Проверка перехода из ЛК по клику на «Конструктор»
    def test_navigate_from_personal_account_to_constructor_by_header_success(self, driver, login):
        self.navigate_to_personal_account(driver)
        self.click_on_constructor_header(driver)
        self.verify_constructor_page_is_displayed(driver)

    # Проверка перехода из ЛК по клику на лого
    def test_navigate_from_personal_account_to_constructor_by_logo_success(self, driver, login):
        self.navigate_to_personal_account(driver)
        self.click_on_logo(driver)
        self.verify_constructor_page_is_displayed(driver)

    # Переход в личный кабинет
    def navigate_to_personal_account(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.profile))
    # Клик на заголовок конструктора
    def click_on_constructor_header(self, driver):
        driver.find_element(*TestLocators.header_of_page_constructor).click()

    # Клик на логотип
    def click_on_logo(self, driver):
        driver.find_element(*TestLocators.logo).click()

    # Проверка, что страница конструктора отображается
    def verify_constructor_page_is_displayed(self, driver):
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
        assert driver.find_element(*TestLocators.button_make_the_order).is_displayed(), \
            "Кнопка 'Оформить заказ' не отображается на странице конструктора."