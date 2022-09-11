from selenium.webdriver.common.by import By

class BasePageLocators():
    MAIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/'

class LoginPageLocators():
        LOGIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        GO_TO_LOGIN_PAGE_BUTTON = (By.XPATH, '//a[@href="/en-gb/accounts/login/"]')
        REGISTER_EMAIL_FIELD = (By.ID, 'id_registration-email')
        REGISTER_PASSWORD_FIELD = (By.ID, 'id_registration-password1')
        REGISTER_CONFIRM_PASSWORD_FIELD = (By.ID, 'id_registration-password2')
        FINISH_REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')
        SUCCESS_MESSAGE_ABOUT_REGISTRATION = (By.XPATH, '//div[@class="alertinner wicon"]')


