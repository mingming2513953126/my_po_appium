#!/usr/bin/python
 # -*- coding: utf-8 -*-
# from time import sleep
import unittest
from time import sleep

from Public import myunit
from shouye.home_page import Home_page
from zhanghu.chongzhi import ChongzhiPage
from zhanghu.login_page import LoginPage
from zhanghu.tixian import TixianPage


class TixianTest(myunit.MyTest):
	def test_Tixian(self):
		u'''充值'''
		pohome = Home_page()
		sleep(7)
		pohome.myaccount()
		popage = LoginPage()
		popage.login('13011111103', '111111')
		pochongzhi = TixianPage()
		# pochongzhi.chongzhi_Action('金额', '111111')
		pochongzhi.tixian_Action('10', '111111')
		sleep(10)


if __name__ == "__main__":
	unittest.main()