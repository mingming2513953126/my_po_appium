# -*- coding: utf-8 -*-
# from time import sleep
import unittest,random, sys, time, os
from time import sleep
from PO.login_page import LoginPage

from PO.BasePage import Page
from Public import myunit

class LoginTest(myunit.MyTest):
	def test_Login(self):
		u'''登录'''
		# pass
		# popage = Swipeleft(self.driver)
		popage = LoginPage(self.driver)
		sleep(5)
		# popage.swipe_Rigth()
		# popage.swipe_Rigth()
		# popage.swipe_Rigth()
		# 用for循环控制多次执行一个自定义函数
		# for i in range(1, 3):
		# 	popage.swipe_Rigth()

		# map(lambda x: popage.swipe_Rigth(), range(0, 3))
		sleep(3)
		popage.login1_Action('13011111101', '111111')
		# popage.login2_Action('13011111101', '111111')


if __name__ == "__main__":
	unittest.main()