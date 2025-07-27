from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from pages.base_page import Page
from selenium.webdriver.common.by import By
import time

class MainPage(Page):
    CONNECT_THE_DEVELOPER = (By.CSS_SELECTOR, '[href="https://www.reelly.ai/for-developer"]')
    MENU = (By.CSS_SELECTOR, 'a.new-market-menu-button._1.w-inline-block')
    MOBILE_MENU = (By.CLASS_NAME, '".new-market-menu-button._1.w-inline-block"')
    CONNECT_MOBILE = (By.CSS_SELECTOR, 'a[href="https://www.reelly.ai/for-developer"]')
    CONNECT_MOBILE_XPATH = (By.XPATH, '//a[.//text()[normalize-space()="Reelly for developer"]]')

    def click_connect_button(self):
        self.verify_partial_url('https://soft.reelly.io/')
        sleep(5)
        #self.wait_for_element(*self.CONNECT_THE_DEVELOPER)
        self.click(*self.CONNECT_THE_DEVELOPER)


    def verify_correct_tab(self):
        self.switch_to_new_window()

    def click_mobile_menu(self):
        sleep(2)
        self.wait_for_element(*self.MENU)
        self.click(*self.MENU)

    def click_mobile_connect_button(self):
        try:
            self.verify_partial_url('https://soft.reelly.io/settings')
            #self.click_mobile_menu()

            # Wait until the link exists in the DOM
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://www.reelly.ai/for-developer"]'))
            )

            # Find the scrollable container
            scroll_container = self.driver.find_element(By.CLASS_NAME, 'settings-block-menu')

            # Scroll to the bottom of the container to reveal the link
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scroll_container)

            time.sleep(1)  # Let the scroll settle

            # Highlight for debug (optional)
            self.driver.execute_script("arguments[0].style.border='2px solid red';", element)

            # Click the link with JavaScript
            self.driver.execute_script("arguments[0].click();", element)
            print("✅ Clicked 'Reelly for developer' link via JS")

        except Exception as e:
            print("❌ Error clicking mobile connect link:", e)
            self.driver.save_screenshot("click_mobile_error.png")










