import os
import datetime

class AllureReporter:
    def __init__(self):
        self.report_directory = "/Users/tamil/Desktop/PythonSeleniumDemo/Projects/Report"

    def generate_report(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        timestamped_folder = f"{self.report_directory}_{timestamp}"
        allure_command = f"allure generate {self.report_directory} -o {timestamped_folder}"
        os.system(allure_command)

if __name__ == "__main__":
    allure_reporter = AllureReporter()
    allure_reporter.generate_report()
