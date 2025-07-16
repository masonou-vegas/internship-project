from pages.base_page import Page
from selenium.webdriver.common.by import By

class LoginPage(Page):

    EMAIL = (By.ID, 'email-2')
    PASSWORD = (By.ID, 'field')
    CONTINUE = (By.CSS_SELECTOR, '[wized="loginButton"]')

    def open_login_page(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def enter_email(self, email):
        self.input_text(email, *self.EMAIL)


    def enter_password(self, password):
        self.input_text(password, *self.PASSWORD)

    def click_continue(self):
        self.click(*self.CONTINUE)
