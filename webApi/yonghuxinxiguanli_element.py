"""用户信息管理element"""
from selenium.webdriver.common.by import By
class yonghuxinxiguanli(object):
	"""docstring for yonghuxinxiguanli"""
	def __init__(self):
		self.menu=(By.XPATH,".//*[@id='app']/div[4]/header/nav/ul/li[4]") #运营管理
		self.link=(By.XPATH,".//*[@id='app']/div[4]/div/section[1]/nav/ul/li[6]/p") #长租管理
		self.userinfo_link=(By.XPATH,".//*[@id='app']/div[4]/div/section[1]/nav/ul/li[6]/ul/li[1]") #用户信息管理
		"""选择137停车场"""
		self.select_137park=(By.XPATH,"html/body/div[1]/div[1]/form/div[1]/div/div/div/div[1]/input")
		self.selected_137park=(By.XPATH,"html/body/div[1]/div[1]/form/div[1]/div/div/div/div[2]/ul[2]/li[7]")

		"""点击创建用户"""
		self.button_add_userinfo=(By.XPATH,"html/body/div[1]/div[2]/div[1]/span[1]")#新建用户按钮
		self.select_park=(By.XPATH,"html/body/div[1]/div[2]/div/form/div/div[1]/div[1]/div/div/div/div[1]/input")#停车场下拉框
		self.selected_park=(By.XPATH,"html/body/div[1]/div[2]/div/form/div/div[1]/div[1]/div/div/div/div[2]/ul[2]/li[7]") #选择137停车场
		self.select_usergroup=(By.XPATH,"html/body/div[1]/div[2]/div/form/div/div[1]/div[2]/div/div/div[1]/input")#选择用户组下拉框
		self.selected_usergroup=(By.XPATH,"html/body/div[1]/div[2]/div/form/div/div[1]/div[2]/div/div/div[2]/ul[2]/li[1]")#选择第一个用户组
		self.input_username=(By.XPATH,"html/body/div[1]/div[2]/div/form/div/div[2]/div[1]/div/div[1]/div/div/input")#用户姓名输入框
		self.input_userphone=(By.XPATH,"html/body/div[1]/div[2]/div/form/div/div[2]/div[2]/div/div/div/div/input")#用户手机号输入框
		self.input_user_carenum=(By.XPATH,"html/body/div[1]/div[2]/div/form/div/div[2]/div[3]/div/div/div/div/input")#用户车牌号输入框
		self.button_save=(By.XPATH,"html/body/div[1]/div[3]/button[1]")#保存按钮

		"""购买长租产品操作"""
		self.user_details=(By.XPATH,"html/body/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[9]/span[1]") #详情按钮
		self.button_purchase=(By.XPATH,"html/body/div[1]/div[3]/div/div[2]/span[1]") #购买产品按钮
		self.select_Long_lease_product_name=(By.XPATH,"html/body/div[1]/div[2]/div/div[1]/form/div[2]/div/div/div[1]/span[1]") #选择产品名称
		self.selected_product=(By.XPATH,"html/body/div[1]/div[2]/div/div[1]/form/div[2]/div/div/div[2]/ul[2]/li[1]") #选择第一个
		self.start_time=(By.XPATH,"html/body/div[1]/div[2]/div/div[1]/form/div[3]/div/div/div[1]/div/input") #开始时间
		self.select_start_time=(By.XPATH,"html/body/div[1]/div[2]/div/div[1]/form/div[3]/div/div/div[2]/div/div/div[2]/div[1]/span[19]/em") #选择12月13日
		self.button_sure_time=(By.XPATH,"html/body/div[1]/div[2]/div/div[1]/form/div[3]/div/div/div[2]/div/div/div[3]/button[2]") #确认选择的时间
		self.agree=(By.XPATH,"html/body/div[1]/div[3]/div/div/label/span/input") #同意合同
		self.button_submit_order=(By.XPATH,"html/body/div[1]/div[3]/button[1]") #提交订单按钮

		"""支付"""
		self.button_payment=(By.XPATH,"/html/body/div[1]/div[3]/button[1]") #支付按钮
		self.pay_by_cash=(By.XPATH,"/html/body/div[1]/div[5]/div[1]/div[1]/div[3]/div/p") #选择现金支付
		self.pay_cash=(By.XPATH,"/html/body/div[1]/div[5]/div[1]/div[4]/div[3]/div/p") #现金支付
		self.return_list=(By.XPATH,"/html/body/div[1]/div[3]/button") #返回列表按钮
		self.return_list_=(By.XPATH,"/html/body/div[1]/div[8]/button") #返回列表
