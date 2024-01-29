from behave import given, when, then, step
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.razor import GillettePage 
import allure

@allure.step
@given(u'I am on the Gillette website')
def step_impl(context):
    try:
        print("Navigating to Gillette website...")
        gillette_page = GillettePage(context.driver)
        gillette_page.open()
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot_after_open", attachment_type=allure.attachment_type.PNG)
        
    except Exception as e:
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        raise e

@allure.step
@when(u'I search for "Razor" using the search option')
def step_impl(context):
    try:
        print("Searching for 'Razor'...")
        gillette_page = GillettePage(context.driver)
        gillette_page.click_search_box() and gillette_page.enter_search_query()
          
    except Exception as e:
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", attaqchment_type=allure.attachment_type.PNG)
        raise e

@allure.step
@then(u'I should see "Results For Razor\'" at the top of the search results')
def step_impl(context):
    try:
        print("Verifying search results...")
        gillette_page = GillettePage(context.driver)
        gillette_page.submit_search()
    except Exception as e:
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        raise e
