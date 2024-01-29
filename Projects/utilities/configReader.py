import configparser

class ConfigReader:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('/Users/tamil/Desktop/PythonSeleniumDemoBDD/Projects/config/config.properties')

    def get_url(self):
        return self.config['DEFAULT']['url']

    def get_browser_name(self):
        return self.config['DEFAULT']['browserName']
    
    def get_url2(self):
        return self.config['DEFAULT']['url2']

