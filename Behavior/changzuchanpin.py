#长租管理--长租产品管理
import sys
sys.path.append('../webApi')
sys.path.append('../common')
sys.path.append('../Data')
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest
import datetime
from logger import Log
from selenium.webdriver.common.by import By
from Changzuchanpingguanli_element import Changzuchanpin_element
from test_data import prodect_name
nowTime=datetime.datetime.now().strftime('%Y-%m-%d:%H:%M:%S')
prodect_name=prodect_name()



class Add_Project(unittest.TestCase,Changzuchanpin_element):
	global prodect_name
	"""初始化element"""
	def __init__(self):
		Changzuchanpin_element.__init__(self)

	def Add_project(self,driver):
		"""新增长租产品"""
		try:
			"""打开长租管理页面"""
			driver.find_element(*self.menu).click()
			sleep(5)
			driver.find_element(*self.link).click()
			sleep(5)
			driver.find_element(*self.Changzu_link).click()
			"""选择137停车场"""
			driver.switch_to.frame("iframeId")
			driver.find_element(*self.park_select).click()
			driver.find_element(*self.park_select).send_keys("137")
			driver.find_element(*self.selectde_park).click()
			sleep(3)
			"""点击新增长租产品按钮"""
			driver.find_element(*self.button_new_project).click()
			sleep(3)
			"""输入相关信息"""
			driver.find_element(*self.project_name).click()
			driver.find_element(*self.project_name).clear()
			driver.find_element(*self.project_name).send_keys(prodect_name)
			Log().info("长租产品名称为：%s"%prodect_name)
			sleep(3)
			driver.find_element(*self.project_type).click()
			sleep(3)
			driver.find_element(*self.selected_project_type).click()
			sleep(3)
			driver.find_element(*self.by_unit).click()
			sleep(3)
			driver.find_element(*self.selected_by_unit).click()
			sleep(3)
			driver.find_element(*self.input_money).click()
			driver.find_element(*self.input_money).clear()
			driver.find_element(*self.input_money).send_keys("0.02")
			sleep(3)
			driver.find_element(*self.input_parkid_mun).click()
			driver.find_element(*self.input_parkid_mun).clear()
			driver.find_element(*self.input_parkid_mun).send_keys("100")
			sleep(3)
			driver.find_element(*self.input_min_mun).click()
			driver.find_element(*self.input_min_mun).clear()
			driver.find_element(*self.input_min_mun).send_keys("1")
			sleep(3)
			driver.find_element(*self.input_max_num).click()
			driver.find_element(*self.input_max_num).clear()
			driver.find_element(*self.input_max_num).send_keys("100")
			sleep(3)
			driver.find_element(*self.project_enable_begindate).click()
			sleep(1)
			driver.find_element(*self.selected_enable_begindate).click()
			sleep(1)
			driver.find_element(*self.project_enable_enddate).click()
			sleep(1)
			driver.find_element(*self.next_month).click()
			sleep(1)
			driver.find_element(*self.selected_enable_enddate).click()

			sleep(3)
			driver.find_element(*self.project_by_begindate).click()
			sleep(1)
			driver.find_element(*self.selected_by_begindate).click()
			sleep(1)
			driver.find_element(*self.project_by_enddate).click()
			sleep(1)
			driver.find_element(*self.by_next_month).click()
			sleep(1)
			driver.find_element(*self.selected_by_enddate).click()

			sleep(3)
			driver.find_element(*self.allow_xufei).click()
			driver.find_element(*self.user_message).click()
			driver.find_element(*self.park_message).click()
			driver.find_element(*self.check).click()
			driver.find_element(*self.second_check).click()
			sleep(3)
			driver.find_element(*self.button_save).click()

		except Exception as e:
			raise e
			print(e)
		finally:
			driver.switch_to.default_content()
