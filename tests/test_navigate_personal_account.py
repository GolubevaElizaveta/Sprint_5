from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.locators import TestLocators
from conftest import driver, login


class TestNavigateToPersonalAccount:
    # Проверка перехода из конструктора бургеров в личный кабинет
    def test_navigate_from_constructor_to_personal_account(self, driver, login):
        self.navigate_to_personal_account(driver)
        self.verify_profile_is_displayed(driver)

    def navigate_to_personal_account(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()

    # Проверка, что профиль отображается
    def verify_profile_is_displayed(self, driver):
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.profile))
        assert driver.find_element(*TestLocators.order_history).is_displayed(), \
            "Профиль не отображается."