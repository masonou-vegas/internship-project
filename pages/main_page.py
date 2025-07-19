from time import sleep

from pages.base_page import Page
from selenium.webdriver.common.by import By
import time

class MainPage(Page):
    CONNECT_THE_DEVELOPER = (By.CSS_SELECTOR, '[href="https://www.reelly.ai/for-developer"]')

    def click_connect_button(self):
        self.verify_partial_url('https://soft.reelly.io/')
        sleep(5)
        #self.wait_for_element(*self.CONNECT_THE_DEVELOPER)
        self.click(*self.CONNECT_THE_DEVELOPER)


    def verify_correct_tab(self):
        self.switch_to_new_window()