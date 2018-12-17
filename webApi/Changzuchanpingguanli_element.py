from selenium.webdriver.common.by import By
from selenium import webdriver
class Changzuchanpin_element(object):
	"""docstring for Changzuchanpin_element"""
	def __init__(self):
		self.menu=(By.XPATH,".//*[@id='app']/div[4]/header/nav/ul/li[4]") #运营管理
		self.link=(By.XPATH,".//*[@id='app']/div[4]/div/section[1]/nav/ul/li[6]/p") #长租管理
		self.Changzu_link=(By.XPATH,".//*[@id='app']/div[4]/div/section[1]/nav/ul/li[6]/ul/li[3]") #长租产品管理
		self.park_select=(By.XPATH,"html/body/div[1]/div[1]/form/div[1]/div/div/div/div[1]/input") #选择停车场下拉框
		self.selectde_park=(By.XPATH,"html/body/div[1]/div[1]/form/div[1]/div/div/div/div[2]/ul[2]/li[7]") #选择137停车场
		self.button_new_project=(By.XPATH,"html/body/div[1]/div[2]/div[1]/span[1]") #新增长租产品		
		self.project_name=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[1]/div/div/input") #长租产品名称
		self.project_type=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[3]/div/div/div[1]/span[1]") #产品类型选择框
		self.selected_project_type=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[3]/div/div/div[2]/ul[2]/li[4]") #类型为137包月组
		self.by_unit=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[5]/div/div/div[1]/span[1]") #购买单位选择框
		self.selected_by_unit=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[5]/div/div/div[2]/ul[2]/li[4]") #购买单位选择“月”		
		self.input_money=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[6]/div/div/div[1]/div/input") #出租单价输入框
		self.input_parkid_mun=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[7]/div/div/input") #发布车位数量输入框
		self.input_min_mun=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[8]/div/div/input") #最小购买数量
		self.input_max_num=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[9]/div/div/input") #最大购买数量
		
		"""产品可用日期选择"""
		self.project_enable_begindate=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[10]/div/div/div[1]/div/div/div[1]/div/input") #产品可用开始日期
		self.selected_enable_begindate=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[10]/div/div/div[1]/div/div/div[2]/div/div/div[2]/div[1]/span[19]/em") #开始日期为今天
		self.project_enable_enddate=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[10]/div/div/div[2]/div/div/div[1]/div/input") #产品可用结束日期
		self.next_month=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[10]/div/div/div[2]/div/div/div[2]/div/div/div[1]/span[6]/i") #点击下一月
		self.selected_enable_enddate=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[10]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/span[15]/em") #选择结束日期

		"""可购买日期选择"""
		self.project_by_begindate=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[11]/div/div/div[1]/div/div/div[1]/div/input") #产品可购买开始日期
		self.selected_by_begindate=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[11]/div/div/div[1]/div/div/div[2]/div/div/div[2]/div[1]/span[19]/em") #开始日期为今天
		self.project_by_enddate=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[11]/div/div/div[2]/div/div/div[1]/div/input") #产品可购买结束日期
		self.by_next_month=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[11]/div/div/div[2]/div/div/div[2]/div/div/div[1]/span[6]/i") #点击下一月
		self.selected_by_enddate=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[1]/div/div[11]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/span[15]/em") #选择结束日期

		self.allow_xufei=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[2]/div/div[1]/div/label") #允许续费
		self.user_message=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[2]/div/div[2]/div/label[1]") #允许短信通知用户
		self.park_message=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[2]/div/div[2]/div/label[2]") #允许短信通知车场
		self.check=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[2]/div/div[2]/div/label[3]") #审核
		self.second_check=(By.XPATH,"html/body/div[1]/div[2]/form/div/div[2]/div/div[2]/div/label[4]") #二级审核
		self.button_save=(By.XPATH,"html/body/div[1]/div[3]/button[1]") #保存按钮

