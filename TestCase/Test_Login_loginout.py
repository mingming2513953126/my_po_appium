#!/usr/bin/python
 # -*- coding: utf-8 -*-
# from time import sleep
import unittest
from time import sleep

from Public import myunit
from shouye.home_page import Home_page
from zhanghu.account.tuichu import TuichuPage
from zhanghu.login_page import LoginPage


class LoginTest(myunit.MyTest):
	def test_Login(self):
		u'''登录'''
		pohome = Home_page()
		sleep(7)
		pohome.myaccount()
		popage = LoginPage()
		popage.login('13011111101', '111111')
		sleep(2)
		pologinout = TuichuPage()
		pologinout.tuichudenglu_Action()
		sleep(10)


if __name__ == "__main__":
	unittest.main()