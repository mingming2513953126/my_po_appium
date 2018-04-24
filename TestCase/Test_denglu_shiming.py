#!/usr/bin/python
 # -*- coding: utf-8 -*-
# from time import sleep
import unittest
from time import sleep

from Public import myunit
from shouye.home_page import Home_page
from zhanghu.account.shiming import Shiming
from zhanghu.login_page import LoginPage
from zhanghu.account.shezhijiaoyimima import Shezhijiaoyimima


class LoginTest(myunit.MyTest):
	def test_Login_shiming_shezhijiaoyimima(self):
		u'''登录,实名，设置交易密码'''
		pohome = Home_page()
		sleep(7)
		pohome.myaccount()
		popage = LoginPage()
		# popage.usr_pwd_button('13511324283', '111111')
		popage.login('13511324283', '111111')
		poshiming = Shiming()
		# poshiming.shiming_Action('姓名', '身份证', '银行卡', '手机')
		poshiming.shiming_Action('李测试账户八', '310101198812177516', '3005457710442524', '15120080522')
		# poshezhijiaoyimima = Shezhijiaoyimima()
		# poshezhijiaoyimima.shezhijiaoyimima_Action()




if __name__ == "__main__":
	unittest.main()