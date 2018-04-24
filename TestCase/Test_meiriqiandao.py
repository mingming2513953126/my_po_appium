#!/usr/bin/python
 # -*- coding: utf-8 -*-
# from time import sleep
import unittest
from time import sleep
from tool.deco import exe_deco
from tool.driver import Appium
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
		popage.login('13011111101', '111111')
		pohome.meiriqiandao_Action()
		pojietu = Appium()
		sleep(1)
		pojietu.get_screenshot_as_file("F:\\work\\python\\jietu\\"+"签到成功.png")
		sleep(10)


if __name__ == "__main__":
	unittest.main()