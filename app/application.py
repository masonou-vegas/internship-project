from pages.base_page import Page
from pages.login_page import LoginPage
from pages.main_page import MainPage



class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        # self.cart_page = CartPage(driver)
        # self.privacy_policy_page = PrivacyPolicyPage(driver)
        # self.target_app_page = TargetAppPage(driver)
        # self.terms_page = TermsPage(driver)
        # self.header = Header(driver)
        #
        # self.search_results_page = SearchResultsPage(driver)
        # self.sign_in_page = SignIn(driver)