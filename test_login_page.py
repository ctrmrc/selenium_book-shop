from pages.locators import BasePageLocators
from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from pages.login_page import LoginPage

def test_guests_can_go_to_login_page(driver):
    url = BasePageLocators.MAIN_PAGE_LINK
    page = BasePage(driver, url)
    page.open()

    page.go_to_login_page()
    page.login_page_has_loggin_in_the_link()

def test_guests_can_registrate(driver):
    url = LoginPageLocators.LOGIN_PAGE_LINK
    page = LoginPage(driver, url)
    page.open()

    email, password = page.email_n_password_gen()

    page.guests_can_registrate(email, password)


