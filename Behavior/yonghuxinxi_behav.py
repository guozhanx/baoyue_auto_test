#运营管理-长租管理-用户信息管理
import sys
sys.path.append('../webApi')
sys.path.append('../Data')
sys.path.append('../common')
from logger import Log
from test_data import username,carnum
from yonghuxinxiguanli_element import yonghuxinxiguanli
import unittest
from time import sleep
username=username()
carnum=carnum()


class Add_userinfo(unittest.TestCase,yonghuxinxiguanli):
	global username,carnum
	def __init__(self):
		yonghuxinxiguanli.__init__(self)

	def open_userinfo(self,driver):
		try:
			"""打开运营管理-长租管理-用户信息管理"""
			driver.find_element(*self.menu).click()
			sleep(3)
			driver.find_element(*self.link).click()
			sleep(3)
			driver.find_element(*self.userinfo_link).click()
			sleep(3)
		except Exception as e:
			raise e
		finally:
			pass

	def add_userinfo(self,driver):
		"""创建用户"""
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
			"""点击创建用户按钮"""
			driver.find_element(*self.button_add_userinfo).click()
			sleep(2)
			driver.find_element(*self.select_park).click()
			sleep(2)
			driver.find_element(*self.select_park).send_keys("137")
			sleep(2)
			driver.find_element(*self.selected_park).click()
			sleep(2)
			driver.find_element(*self.select_usergroup).click()
			sleep(2)
			driver.find_element(*self.selected_usergroup).click()
			sleep(2)
			text=driver.find_element(*self.selected_usergroup).text
			Log().info('用户组选择第一个：%s'%text)

			driver.find_element(*self.input_username).send_keys(username)
			Log().info("用户名称为：%s"%username)

			driver.find_element(*self.input_userphone).send_keys("18500021021")

			driver.find_element(*self.input_user_carenum).send_keys(carnum)
			Log().info("输入的车牌号：%s"%carnum)

			
			"""点击保存按钮"""
			driver.find_element(*self.button_save).click()
			sleep(10)
		except Exception as e:
			raise e
		finally:
			driver.switch_to.default_content()

	def buy_prodect(self,driver):
		"""购买长租产品"""
		try:
			driver.switch_to.frame("iframeId")
			driver.find_element(*self.user_details).click()
			sleep(2)
			driver.find_element(*self.button_purchase).click()
			sleep(2)
			driver.find_element(*self.select_Long_lease_product_name).click()
			sleep(2)
			text=driver.find_element(*self.selected_product).text
			Log().info('选择的长租产品名称为：%s'%text)
			sleep(3)
			driver.find_element(*self.selected_product).click()
			sleep(2)
			driver.find_element(*self.start_time).click()
			sleep(2)
			driver.find_element(*self.select_start_time).click()
			sleep(2)
			driver.find_element(*self.button_sure_time).click()
			sleep(2)
			driver.find_element(*self.agree).click()
			sleep(2)
			driver.find_element(*self.button_submit_order).click()
			sleep(2)
		except Exception as e:
			raise e
			print(e)
			Log().info(e)
			Log().error(e)
		'''finally:
			driver.switch_to.default_content()'''

	def pay_prodect(self,driver):
		"""长租产品现金支付"""
		try:
			sleep(2)
			driver.find_element(*self.button_payment).click()
			sleep(2)
			driver.find_element(*self.pay_by_cash).click()
			sleep(2)
			driver.find_element(*self.pay_cash).click()
			sleep(2)
			driver.find_element(*self.return_list).click()
			sleep(2)
			driver.find_element(*self.return_list_).click()
			sleep(5)
		except Exception as e:
			raise e
			Log().info(e)
			Log().error(e)
		finally:
			driver.switch_to.default_content()
		
