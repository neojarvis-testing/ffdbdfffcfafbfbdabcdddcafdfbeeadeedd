from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from utilities.eventhandler import EventHandler

def before_all(context):
    event_handler = EventHandler()
    options = webdriver.ChromeOptions()
    print("Instance created")
    options.add_argument("--start-maximized")
    remote_url = "https://4444-seleniuminstance3.premiumproject.examly.io"
    base_driver = webdriver.Remote(command_executor=remote_url, options=options)
    context.driver = EventFiringWebDriver(base_driver, event_handler)


def after_all(context):
    print("instance Destroyed")
    context.driver.quit()
