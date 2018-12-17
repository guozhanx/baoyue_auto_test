"""
集团信息管理-用户组信息管理-新建用户组：用户组名称和描述的参数
"""
import random
"""生成用户名"""
def username():
	randomdata = range(99,999)
	randomlist = random.sample(randomdata,1)
	str1="User_"
	return(str1+str(randomlist))
"""生成车牌号"""
def carnum():
	randomdata=range(88888,99999)
	randomlist = random.sample(randomdata,1)
	str1="台B"
	return(str1+str(randomlist[0]))

"""生成用户组名"""
def user_group_name():
	randomdata = range(99,999)
	randomlist = random.sample(randomdata,1)
	str1="UGN_"
	return(str1+str(randomlist))

"""生成长租产品名"""
def prodect_name():
	randomdata = range(99,999)
	randomlist = random.sample(randomdata,1)
	str1="ProName_"
	return(str1+str(randomlist))
