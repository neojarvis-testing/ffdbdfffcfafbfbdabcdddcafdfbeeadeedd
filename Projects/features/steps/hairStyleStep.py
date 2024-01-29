from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.HairStyle import HairStylePage
from utilities.configReader import ConfigReader
import time
import allure

@allure.step
@given(u'I am on the Gillette website to look for styling')
def step_impl(context):
    try:
        config = ConfigReader()
        url = config.get_url()
        context.driver.get(url)
        
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot_after_open", attachment_type=allure.attachment_type.PNG)

    except Exception as e:
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        raise e

@allure.step
@when(u'I click on "Styling" under "Learn" in the footer')
def step_impl(context):
    try:
        hairStyle = HairStylePage(context.driver)  
        time.sleep(10)
        hairStyle.click_styles()
    except Exception as e:
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        raise e

@allure.step
@then(u'I should see "Facial Hair Styles: The Anchor Beard" under the list of articles under styling')
def step_impl(context):
    try:
        hairStyle = HairStylePage(context.driver)  
        hairStyle.click_facial()
        time.sleep(10)
    except Exception as e:
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        raise e

        

