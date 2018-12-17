#coding:utf-8   #强制使用utf-8编码格式

import smtplib,sys
from email.mime.text import MIMEText  
import email.mime.multipart
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
#sys.path.append('../common')
#import find_report
#my_sender='发件人邮箱账号' #发件人邮箱账号，为了后面易于维护，所以写成了变量
#my_user='收件人邮箱账号' #收件人邮箱账号，为了后面易于维护，所以写成了变量
#report_dir=find_report.new_report_name()

class SendEmail:
	"""docstring for SendEmail"""
	def __init__(self,recevier_email,Subject,report_dir):
		self.recevier_email = recevier_email
		self.sender_email='Guozhanxiu126@126.com'
		self.Subject=Subject
		self.report_dir=report_dir

	def mail(self):
		try:
			content = '自动化测试报告（包月），详情请下载附件查看！'#邮件正文
			msg = MIMEMultipart()
			body = MIMEText(content, _subtype='html', _charset='gb2312')  # 创建一个实例，这里设置为html格式邮件
			msg.attach(body)
			msg['From']=self.sender_email  #括号里的对应发件人邮箱昵称、发件人邮箱账号
			msg['To']=self.recevier_email   #括号里的对应收件人邮箱昵称、收件人邮箱账号
			msg['Subject']=self.Subject #邮件的主题，也可以说是标题

			part = MIMEApplication(open(self.report_dir,'rb').read())
			part.add_header('Content-Disposition', 'attachment', filename=self.report_dir)
			msg.attach(part)

			server=smtplib.SMTP("smtp.126.com",25)  #发件人邮箱中的SMTP服务器，端口是25
			server.login(self.sender_email,"gzx130mima")    #括号中对应的是发件人邮箱账号、邮箱密码
			server.sendmail(self.sender_email,[self.recevier_email,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
			server.quit()   #这句是关闭连接的意思
		except Exception as e:
			print(e)   #如果try中的语句没有执行，则会执行下面的ret=False

'''
if __name__ == '__main__':


	sender=SendEmail('1060859676@qq.com','自动化测试报告')
	sender.mail()'''



