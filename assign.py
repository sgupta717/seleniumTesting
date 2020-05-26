import unittest
import time
from selenium import webdriver

class TestLaunch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("D:\\Programs\\STP\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
        self.driver.maximize_window()
        time.sleep(2)

    def test_alert(self):
        #For Alert Button
        self.driver.find_element_by_xpath("//button[contains(@onclick,'Alert')]").click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()

        #For Confirm Button
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,200)")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(@onclick,'Confirm')]").click()
        self.driver.switch_to.alert
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(@onclick,'Confirm')]").click()
        self.driver.switch_to.alert
        time.sleep(2)
        self.driver.switch_to.alert.dismiss()

        #For Prompt Button
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,600)")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(@onclick,'Prompt')]").click()
        time.sleep(1)
        self.driver.switch_to.alert.send_keys('RVCE')
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)

        def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()