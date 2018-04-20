 # -*- coding: utf-8 -*-
# from time import sleep
import unittest
 from time import sleep
from zhanghu.login_page import LoginPage
from shouye.home_page import Home_page
 from Public import myunit
 import unittest
 from time import sleep

 from Public import myunit
 from shouye.home_page import Home_page
 from zhanghu.login_page import LoginPage


 class RegisterTest(myunit.MyTest):
	def test_Register(self):
		u'''登录'''
		pohome = Home_page(self.driver)
		sleep(7)
		pohome.home_account()
		poaccount = LoginPage(self.driver)
		poaccount.go_register_Action()




if __name__ == "__main__":
	unittest.main()