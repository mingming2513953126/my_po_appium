#!/usr/bin/python
 # -*- coding: utf-8 -*-
# from time import sleep
import unittest
from time import sleep

from Public import myunit
from shouye.home_page import Home_page
from zhanghu.login_page import LoginPage


class LoginTest(myunit.MyTest):
	def test_Login(self):
		u'''登录'''
		pohome = Home_page()
		sleep(7)
		pohome.myaccount()
		popage = LoginPage()
		# sleep(7)
		# popage.swipe_Rigth()
		# popage.swipe_Rigth()
		# popage.swipe_Rigth()
		# 用for循环控制多次执行一个自定义函数
		# for i in range(1, 3):
		# 	popage.swipeRight()

		# map(lambda x: popage.swipe_Rigth(), range(0, 3))
		# popage.usr_pwd_button('13011111111', '111111')
		# popage.login2_Action('13011111101', '111111')
		popage.login('13011111101', '111111')
		sleep(10)


if __name__ == "__main__":
	unittest.main()