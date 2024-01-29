import logging
from selenium.webdriver.common.by import By
from utilities.excelReader import ExcelReader  
from locaters.uiRazor import RazorUI
from utilities.screenshot import Screenshot
from utilities.webDriverHelper import WebDriverHelper

class GillettePage:
    def __init__(self, driver):
        self.driver = driver
        self.excel_reader = ExcelReader('/Users/tamil/Desktop/PythonSeleniumDemo/Projects/data/Datasheet.xlsx')  
        self.search_queries = self.get_search_queries()  

    def get_search_queries(self):
        data = self.excel_reader.get_data(sheet_name='Sheet1')  
        return [row['Keys'] for row in data] 

    def open(self):
        try:
            self.driver.get("https://www.gillette.co.in")
            logging.info("Gillette page opened successfully.")
            return True
        except Exception as e:
            logging.error(f"Error opening Gillette page: {e}")
            Screenshot.capture_screenshot(self.driver)
            return False

    def click_search_box(self):
        try:
            locator = (By.XPATH, RazorUI.search_icon)
            WebDriverHelper(self.driver).clickElement(locator)
            logging.info("Clicked on Search icon successfully.")
            return True
        except Exception as e:
            logging.error(f"Error while clicking on search icon: {e}")
            Screenshot.capture_screenshot(self.driver)
            return False

    def enter_search_query(self):
        try:
            locator = (By.XPATH, RazorUI.search_box)
            for query in self.search_queries:  
                WebDriverHelper(self.driver).fillForm(locator, query)  
            logging.info("Keys sent to the Search box successfully")
            return True
        except Exception as e:
            logging.error(f"Error while entering search query: {e}")
            Screenshot.capture_screenshot(self.driver)  
            return False

    def submit_search(self):
        try:
            locator = (By.XPATH, RazorUI.select_razor)
            WebDriverHelper(self.driver).clickElement(locator)
            logging.info("Search for Razor successfully")
            return True
        except Exception as e:
            logging.error(f"Error while submitting search: {e}")
            Screenshot.capture_screenshot(self.driver)
            return False
