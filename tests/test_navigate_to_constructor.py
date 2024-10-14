from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.locators import TestLocators
from conftest import driver, login


class TestNavigateToConstructor:
    # Проверка перехода из ЛК по клику на «Конструктор»
    def test_navigate_from_personal_account_to_constructor_by_header_success(self, driver, login):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.profile))
        driver.find_element(*TestLocators.header_of_page_constructor).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
        assert driver.find_element(*TestLocators.button_make_the_order).is_displayed(), \
            "Кнопка 'Оформить заказ' не отображается на странице конструктора."

    # Проверка перехода из ЛК по клику на логотип
    def test_navigate_from_personal_account_to_constructor_by_logo_success(self, driver, login):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.profile))
        driver.find_element(*TestLocators.logo).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
        assert driver.find_element(*TestLocators.button_make_the_order).is_displayed(), \
            "Кнопка 'Оформить заказ' не отображается на странице конструктора."