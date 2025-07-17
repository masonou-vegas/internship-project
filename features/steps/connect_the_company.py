from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open login page')
def open_login_page(context):
    context.app.login_page.open_login_page()

@when('Enter {email} into email')
def enter_email(context, email):
    context.app.login_page.enter_email(email)

@when('Enter {password} into password')
def enter_password(context, password):
    context.app.login_page.enter_password(password)
    sleep(2)

@then('click Continue')
def click_continue_button(context):
    context.app.login_page.click_continue()

@then('Click on “Connect the developer”')
def click_connect_button(context):
    context.app.main_page.click_connect_button()

@then('verify correct tab opens')
def verify_correct_tab(context):
    context.app.main_page.verify_correct_tab()

@then('verify the URL')
def verify_url(context):
    context.app.base_page.verify_url('https://www.reelly.ai/for-developer')