from pages.base_page import Page
from pages.login_page import LoginPage
from pages.main_page import MainPage
#from pages.developer_page import DeveloperPage
# from pages.off_plan_page import OffPlanPage
# from pages.settings_page import SettingsPage
# from pages.subscription_page import SubscriptionPage
# from pages.secondary_page import SecondaryPage
# from pages.registration_page import RegistrationPage

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        #self.developer_page = DeveloperPage(driver)
        # self.off_plan_page = OffPlanPage(driver)
        # self.settings_page = SettingsPage(driver)
        # self.subscription_page = SubscriptionPage(driver)
        # self.secondary_page = SecondaryPage(driver)
        # self.registration_page = RegistrationPage(driver)