from selenium import webdriver
class Config(object):
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "http://prep.tingjiandan.com/bmp-web/login"
		self.verificationErrors = []
		self.accept_next_alert = True