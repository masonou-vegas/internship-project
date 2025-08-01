from time import sleep

from pages.base_page import Page
from selenium.webdriver.common.by import By

class LoginPage(Page):

    EMAIL = (By.ID, 'email-2')
    PASSWORD = (By.ID, 'field')
    CONTINUE = (By.CSS_SELECTOR, '[wized="loginButton"]')

    def open_login_page(self):
        self.driver.get('https://soft.reelly.io/sign-in')
        self.driver.delete_all_cookies()

    def enter_email(self, email):
        sleep(2)
        self.wait_for_element(*self.EMAIL)
        self.input_text(email, *self.EMAIL)


    def enter_password(self, password):
        sleep(2)
        self.input_text(password, *self.PASSWORD)

    def click_continue(self):
        sleep(2)
        self.wait_for_element_click(*self.CONTINUE)
        sleep(2)
        #self.click(*self.CONTINUE)
