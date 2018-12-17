"""用户组管理element"""
from selenium.webdriver.common.by import By
class yonghuzuxinxiguanli(object):
	"""docstring for yonghuzuxinxiguanli"""
	def __init__(self):
		self.menu=(By.XPATH,".//*[@id='app']/div[4]/header/nav/ul/li[4]") #运营管理
		self.link=(By.XPATH,".//*[@id='app']/div[4]/div/section[1]/nav/ul/li[6]/p") #长租管理
		self.usergroup_link=(By.XPATH,".//*[@id='app']/div[4]/div/section[1]/nav/ul/li[6]/ul/li[2]") #用户组管理
		"""选择137停车场"""
		self.select_137park=(By.XPATH,"html/body/div[1]/div[1]/form/div[1]/div/div/div/div[1]/input")
		self.selected_137park=(By.XPATH,"html/body/div[1]/div[1]/form/div[1]/div/div/div/div[2]/ul[2]/li[7]")

		"""点击创建用户组"""
		self.button_add_usergroup=(By.XPATH,"html/body/div[1]/div[2]/div[1]/span[1]")#新建用户组按钮
		self.select_park=(By.XPATH,"html/body/div[1]/div[2]/div/div[1]/div/form/div[1]/div/div/div/div[1]/input")#停车场下拉框
		self.selected_park=(By.XPATH,"html/body/div[1]/div[2]/div/div[1]/div/form/div[1]/div/div/div/div[2]/ul[2]/li[7]") #选择137停车场
		self.usergroup_name=(By.XPATH,"html/body/div[1]/div[2]/div/div[1]/div/form/div[2]/div/div/input")#用户组名称
		self.point_select=(By.XPATH,"html/body/div[1]/div[2]/div/div[1]/div/form/div[3]/div/div/label[1]")#本地是否可编辑
		self.button_save=(By.XPATH,"html/body/div[1]/div[2]/div/div[2]/button[1]")#保存按钮