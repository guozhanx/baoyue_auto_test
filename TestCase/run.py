import unittest
from HTMLTestRunner import HTMLTestRunner
import time,sys
sys.path.append('../common')
from Sendemail import SendEmail
import find_report

test_dir = '.'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

if __name__ == '__main__':
	try:
		now = time.strftime("%Y-%m-%d %H_%M_%S")
		filename = '../report/' + now + '_result.html'
		fp = open(filename, 'wb')
		runner = HTMLTestRunner(stream=fp,title=u'接口自动化测试报告,测试结果如下：',description=u'用例执行情况：')
		runner.run(discover)
		fp.close()
	except Exception as e:
		raise e
	finally:
		report_dir=find_report.new_report_name()
		sender=SendEmail('zhanxiu.guo@tingjiandan.com','自动化测试报告',report_dir).mail()