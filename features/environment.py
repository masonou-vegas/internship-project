from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.chrome.options import Options



def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    #options = Options()
    #options.add_argument("--headless=new")
    #context.driver = webdriver.Chrome(options=options)
    #context.driver = webdriver.Chrome(service=service)

    ### HEADLESS MODE ####
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(options=options)
    #context.driver = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(6)
    context.app = Application(context.driver)

    context.driver.save_screenshot("screenshot.png")
    print(context.driver.page_source)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)



def after_scenario(context, feature):
    context.driver.quit()
