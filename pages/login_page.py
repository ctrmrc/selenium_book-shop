from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def email_n_password_gen(self):
        return (str(time.time()) + '@fakemail.org', 'Pass_6789')

    def guests_can_registrate(self, email, password):
        self.email = email
        self.password = password

        self.driver.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_FIELD).send_keys(password)

        self.driver.find_element(*LoginPageLocators.FINISH_REGISTER_BUTTON).click()

        self.wait_element(*LoginPageLocators.SUCCESS_MESSAGE_ABOUT_REGISTRATION)
        assert 'Thanks for registering!' in self.driver.find_element(*LoginPageLocators.SUCCESS_MESSAGE_ABOUT_REGISTRATION).text, 'There is must be Thanks for registering!'

