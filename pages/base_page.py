from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from .locators import LoginPageLocators

class BasePage(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def wait_element(self, howfindel, whatfind, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((howfindel, whatfind)))
        except NoSuchElementException:
            return True
        return False

    def go_to_login_page(self):
        self.driver.find_element(*LoginPageLocators.GO_TO_LOGIN_PAGE_BUTTON).click()

