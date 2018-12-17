#运营管理-长租管理-用户组管理
import sys
sys.path.append('../webApi')
sys.path.append('../Data')
sys.path.append('../common')
from logger import Log
from test_data import user_group_name
from yonghuzuguanli_element import yonghuzuxinxiguanli
import unittest
from time import sleep
user_group_name=user_group_name()

class Add_usergroup(unittest.TestCase,yonghuzuxinxiguanli):
	global user_group_name
	def __init__(self):
		yonghuzuxinxiguanli.__init__(self)

	def open_usergroup(self,driver):
		try:
			"""打开运营管理-长租管理-用户组管理"""
			driver.find_element(*self.menu).click()
			sleep(3)
			driver.find_element(*self.link).click()
			sleep(3)
			driver.find_element(*self.usergroup_link).click()
			sleep(3)
		except Exception as e:
			raise e
		finally:
			pass

	def add_usergroup(self,driver):
		"""新建用户组"""
		try:
			
			driver.switch_to.frame("iframeId")
			"""选择137停车场"""
			driver.find_element(*self.select_137park).click()
			sleep(2)
			driver.find_element(*self.select_137park).send_keys("137")
			sleep(3)
			driver.find_element(*self.selected_137park).click()
			Log().info('车场选择137测试停车场')
			sleep(2)
			"""点击新建用户"""
			driver.find_element(*self.button_add_usergroup).click()
			sleep(2)
			driver.find_element(*self.select_park).click()
			sleep(2)
			driver.find_element(*self.select_park).send_keys("137")
			sleep(2)
			driver.find_element(*self.selected_park).click()
			sleep(2)
			driver.find_element(*self.usergroup_name).send_keys(user_group_name)
			Log().info("输入新建的用户组名称：%s"%user_group_name)
			sleep(2)
			driver.find_element(*self.point_select).click()
			"""点击保存按钮"""
			driver.find_element(*self.button_save).click()
			sleep(5)
		except Exception as e:
			raise e
		finally:
			driver.switch_to.default_content()
		
