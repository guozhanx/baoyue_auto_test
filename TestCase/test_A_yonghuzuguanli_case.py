import sys
sys.path.append('../Behavior/')
sys.path.append('../common/')
from yonghuzuguanli_beha import Add_usergroup
from Login import Login
from Logout import Logout
import unittest
from selenium import webdriver

class ADD_UserGroup(unittest.TestCase):
	"""新增用户组"""
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "http://prep.tingjiandan.com/bmp-web/login"
		self.verificationErrors = []
		self.accept_next_alert = True
		
	def test_add_usergroup(self):
		"""创建用户组"""
		driver=self.driver
		driver.maximize_window()
		driver.get(self.base_url)
		"""登录B端管理平台"""
		Login().user_login(driver)
		"""打开用户组管理页面"""
		Add_usergroup().open_usergroup(driver)
		"""新建一个用户组"""
		Add_usergroup().add_usergroup(driver)

	def tearDown(self):
		driver = self.driver
		Logout().user_loginout(driver)
		self.driver.quit()

if __name__ == '__main__':
    unittest.main()