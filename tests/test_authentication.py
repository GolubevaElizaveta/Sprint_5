from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.locators import TestLocators
from conftest import driver
from src.data import UsersTestData


class TestAuthentication:
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_via_main_button(self, driver):
        driver.find_element(*TestLocators.button_login_in_main).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.input_email_auth).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.input_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.button_login).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
        assert driver.find_element(*TestLocators.button_make_the_order).is_displayed(), \
            "Кнопка 'Оформить заказ' не отображается после успешного входа."

    # Вход через кнопку «Личный кабинет»
    def test_login_via_personal_account_button(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.input_email_auth).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.input_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.button_login).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
        assert driver.find_element(*TestLocators.button_make_the_order).is_displayed(), \
            "Кнопка 'Оформить заказ' не отображается после успешного входа."

    # Вход через кнопку в форме регистрации
    def test_login_via_registration_form_button(self, driver):
        driver.find_element(*TestLocators.button_login_in_main).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.button_submit))
        driver.find_element(*TestLocators.button_login_in_registration_form).click()
        driver.find_element(*TestLocators.input_email_auth).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.input_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.button_login).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
        assert driver.find_element(*TestLocators.button_make_the_order).is_displayed(), \
            "Кнопка 'Оформить заказ' не отображается после успешного входа."

    # Вход через кнопку в форме восстановления пароля
    def test_login_via_password_recovery_form_button(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_forgot_password).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_login_passwd_recovery_form))
        driver.find_element(*TestLocators.button_login_passwd_recovery_form).click()
        driver.find_element(*TestLocators.input_email_auth).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.input_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.button_login).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
        assert driver.find_element(*TestLocators.button_make_the_order).is_displayed(), \
            "Кнопка 'Оформить заказ' не отображается после успешного входа."
