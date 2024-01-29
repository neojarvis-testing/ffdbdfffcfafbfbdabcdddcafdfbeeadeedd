import logging
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.screenshot import Screenshot
from locaters.uiHairStyle import HairstyleUI
from utilities.webDriverHelper import WebDriverHelper
from utilities.logger import configure_logger

configure_logger()

class HairStylePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        try:
            logging.info("Opening https://www.gillette.co.in")
            self.driver.get("https://www.gillette.co.in")
            logging.info("Website opened successfully.")

        except Exception as e:
            logging.error(f"Error while opening website: {e}")
            Screenshot.capture_screenshot(self.driver)


    def click_styles(self):
        try:
            logging.info("Scrolling down and clicking on Styles.")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            locator = (By.XPATH, HairstyleUI.click_style)
            WebDriverHelper(self.driver).clickElement(locator)
            logging.info("Clicked on Styles successfully.")
        except Exception as e:
            logging.error(f"Error while clicking on Styles: {e}")
            Screenshot.capture_screenshot(self.driver)



    def click_facial(self):
        try:
            logging.info("Clicking on Facial.")
            time.sleep(5)
            locators= (By.XPATH, HairstyleUI.click_facial)
            WebDriverHelper(self.driver).clickElement(locators)
            logging.info("Clicked on Facial successfully.")
        except Exception as e:
            logging.error(f"Error while clicking on Facial: {e}")
            Screenshot.capture_screenshot(self.driver)