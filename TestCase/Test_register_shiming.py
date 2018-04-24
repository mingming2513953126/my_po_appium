# -*- coding: utf-8 -*-
# from time import sleep
import unittest
from time import sleep
from Public import myunit
from shouye.home_page import Home_page
from zhanghu.account.shiming import Shiming
from zhanghu.login_page import LoginPage
from zhanghu.account.zhuce import Zhucepage
from zhanghu.account.shezhijiaoyimima import Shezhijiaoyimima

class RegisterTest(myunit.MyTest):
	def test_register_shiming_shezhijiaoyimima(self):
		u'''注册，实名，设置交易密码'''
		pohome = Home_page()
		sleep(7)
		pohome.home_account()
		poaccount = LoginPage()
		poaccount.go_register_Action()
		pozhuce = Zhucepage()
		pozhuce.zhuce_Action(13011111101, 111111, 111111)
		poshiming = Shiming()
		# poshiming.shiming_Action('姓名', '身份证', '银行卡', '手机')
		poshiming.shiming_Action('', '', '', '')
		poshezhijiaoyimima = Shezhijiaoyimima()
		poshezhijiaoyimima.shezhijiaoyimima_Action()




if __name__ == "__main__":
	unittest.main()