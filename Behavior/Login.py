#登录
import sys
sys.path.append('../webApi')
sys.path.append('../common')
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest
import datetime
from logger import Log
from selenium.webdriver.common.by import By
from Login_Logout_Element import Login_Logout_Element
nowTime=datetime.datetime.now().strftime('%Y-%m-%d:%H:%M:%S')


class Login(unittest.TestCase,Login_Logout_Element):
	"""初始化element"""
	def __init__(self):
		Login_Logout_Element.__init__(self)

	def user_login(self, driver):
		"""登录网站"""
		try:
			#清空用户名输入框
			driver.find_element(*self.username_loc).clear()
			#输入用户名
			driver.find_element(*self.username_loc).send_keys("admin")
			#清空密码输入框
			driver.find_element(*self.password_loc).clear()
			#输入密码
			driver.find_element(*self.password_loc).send_keys("Tjd123456")
			#点击登录按钮
			driver.find_element(*self.submit_loc).click()
			sleep(5)
			#判断是否登录成功
			if driver.title=="停车场智能管理平台":
				Log().info("登录成功！")

			else:
				Log().info("登录失败！")
		except Exception as e:
			Log().error(e)
			raise(e)
