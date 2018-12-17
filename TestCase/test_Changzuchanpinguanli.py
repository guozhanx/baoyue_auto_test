"""长租管理--长租产品管理"""
"""新增长租产品"""

from selenium import webdriver
import unittest,sys
sys.path.append('../Behavior')
sys.path.append('../webApi')
sys.path.append('../common')
from Login import Login
from Logout import Logout
from Changzuchanpingguanli_element import Changzuchanpin_element
from changzuchanpin import Add_Project
from time import sleep

class Add_Project_Test(unittest.TestCase):
    """新增长租产品"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://prep.tingjiandan.com/bmp-web/login"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_Add_project(self):
        """新建长租产品"""
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        Login().user_login(driver)
        Add_Project().Add_project(driver)
        sleep(10)


    def tearDown(self):
        driver = self.driver
        Logout().user_loginout(driver)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
