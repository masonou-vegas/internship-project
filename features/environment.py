from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.application import Application

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    #context.driver = webdriver.Chrome (service=service)

    ##Mobile Emulator##
    #from selenium import webdriver
    #from selenium.webdriver.chrome.options import Options
    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
        "clientHints": {"platform": "Android", "mobile": True}}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)


    ### SAFARI ###
    # context.driver = webdriver.Firefox()
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(
    #     options=options
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user ='masonmcderp_3WJDjn'
    bs_key = 'zwybyEkxyBLrD8ZWx1tM'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        # "os" : "Windows",
        # "osVersion" : "11",
        # 'browserName': 'Edge',
        "deviceName": "Google Pixel 7",  # Choose any available device
        "osVersion": "13.0",  # Match the device's OS
        "realMobile": "true",  # Ensures it's not an emulator
        "browserName": "Chrome",
        'sessionName': scenario_name,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)
    #context.driver = webdriver.Chrome(options=chrome_options)
    #context.driver.maximize_window()
    context.driver.implicitly_wait(6)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
