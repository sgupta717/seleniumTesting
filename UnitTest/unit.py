import unittest
import time
timestr = time.strftime("%y%m%d-%H%M%S")
from selenium import webdriver

class TestLaunch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("D:\\Programs\\STP\\chromedriver_win32\\chromedriver.exe") #Store the webdriver in a particular path and call it within the program
        self.driver.get("D:/Programs/STP/UnitTestAssets/index.html")
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.save_screenshot('D:/Programs/STP/UnitTestAssets/ScreenShots/initial-login.png')
        self.driver.save_screenshot("loginScreenBeforeEnteringTheDetails"+timestr+".png")

    def test_FindClass(self):
        self.driver.find_element_by_id('User').send_keys('admin') #Enter User Name
        self.driver.find_element_by_id('Pass').send_keys('root123') #Enter Password
        self.driver.save_screenshot('D:/Programs/STP/UnitTestAssets/ScreenShots/logincredentials.png')
        self.driver.save_screenshot("logincredentials"+timestr+".png")
        self.driver.find_element_by_css_selector('.login').click()  #clicking login
        self.driver.save_screenshot('D:/Programs/STP/UnitTestAssets/ScreenShots/success-screen.png')
        self.driver.get("D:/Programs/STP/UnitTestAssets/index.html")
        self.driver.find_element_by_id('User').send_keys('admin')  # Enter right User Name
        self.driver.find_element_by_id('Pass').send_keys('root')  # Enter wrong Password
        time.sleep(2)
        self.driver.save_screenshot('D:/Programs/STP/UnitTestAssets/ScreenShots/logincredentials.png')
        self.driver.save_screenshot("logincredentials" + timestr + ".png")
        self.driver.find_element_by_css_selector('.login').click()  # clicking login
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        self.driver.get("D:/Programs/STP/UnitTestAssets/index.html")
        self.driver.find_element_by_id('User').send_keys('adminnnnn')  # Enter wrong User Name
        self.driver.find_element_by_id('Pass').send_keys('root123')  # Enter right Password
        time.sleep(2)
        self.driver.save_screenshot('D:/Programs/STP/UnitTestAssets/ScreenShots/logincredentials.png')
        self.driver.save_screenshot("logincredentials" + timestr + ".png")
        self.driver.find_element_by_css_selector('.login').click()  # clicking login
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        self.driver.get("D:/Programs/STP/UnitTestAssets/index.html")
        self.driver.find_element_by_id('User').send_keys('')  # Enter Empty User Name
        self.driver.find_element_by_id('Pass').send_keys('')  # Enter Empty Password
        time.sleep(2)
        self.driver.save_screenshot('D:/Programs/STP/UnitTestAssets/ScreenShots/logincredentials.png')
        self.driver.save_screenshot("logincredentials" + timestr + ".png")
        self.driver.find_element_by_css_selector('.login').click()  # clicking login
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        self.driver.get("D:/Programs/STP/UnitTestAssets/index.html")
        self.driver.find_element_by_id('User').send_keys('administrator') #Enter wrongUser Name
        self.driver.find_element_by_id('Pass').send_keys('root123') #Enter Password
        time.sleep(2)
        self.driver.save_screenshot('D:/Programs/STP/UnitTestAssets/ScreenShots/wrong-credentials.png')
        self.driver.find_element_by_css_selector('.reset').click()  #clicking reset
        self.driver.save_screenshot('D:/Programs/STP/UnitTestAssets/ScreenShots/reset.png')
        #self.assertTrue(self.driver.find_element_by_xpath(".//label"), "Username")

    def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
