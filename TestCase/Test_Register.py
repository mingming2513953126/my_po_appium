# -*- coding: utf-8 -*-
# from time import sleep
import unittest
from time import sleep

from Public import myunit
from shouye.home_page import Home_page
from zhanghu.login_page import LoginPage
from zhanghu.account.zhuce import Zhucepage

class RegisterTest(myunit.MyTest):
	def test_register(self):
		u'''注册'''
		pohome = Home_page()
		sleep(7)
		pohome.home_account()
		poaccount = LoginPage()
		poaccount.go_register_Action()
		pozhuce = Zhucepage()
		pozhuce.zhuce_Action(13011111101, 111111, 111111)




if __name__ == "__main__":
	unittest.main()