import os
def new_report_name():

	report_dir='..\\report'
	lists=os.listdir(report_dir)

	lists.sort(key=lambda fn:os.path.getmtime(report_dir+"\\"+fn))
	#print(('最新的文件为：'+lists[-1]))
	files=os.path.join(report_dir,lists[-1])
	return(files)

#print(new_report_name())
