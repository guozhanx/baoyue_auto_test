"""长租管理--用户信息管理"""
# -*- coding: utf-8 -*-
import sys
sys.path.append('../Behavior/')
sys.path.append('../common/')
from yonghuxinxi_behav import Add_userinfo
from Login import Login
from Logout import Logout
import unittest
from selenium import webdriver

class ADD_UserInfo(unittest.TestCase):
    """创建用户"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://prep.tingjiandan.com/bmp-web/login"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_add_userinfo(self):
        """创建用户，并购买长租产品并支付现金"""
        driver=self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        """登录B端管理平台"""
        Login().user_login(driver)
        """打开用户信息管理页面"""
        Add_userinfo().open_userinfo(driver)
        """新建一个用户"""
        Add_userinfo().add_userinfo(driver)
        """购买长租产品"""
        Add_userinfo().buy_prodect(driver)
        """长租产品购买支付"""
        Add_userinfo().pay_prodect(driver)
    def tearDown(self):
        driver = self.driver
        Logout().user_loginout(driver)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()