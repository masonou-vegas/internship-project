from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    CONNECT_THE_DEVELOPER = (By.CSS_SELECTOR, '[href="https://www.reelly.ai/for-developer"]')

    def click_connect_button(self):
        self.click(*self.CONNECT_THE_DEVELOPER)

    def verify_correct_tab(self):
        self.switch_to_new_window()