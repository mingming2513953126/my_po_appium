# -*- coding: utf-8 -*-
import os
__author__ = 'JennyHui'
import unittest
# from PO import DashPage
# from selenium import webdriver
from tool.driver import Appium
from appium import webdriver
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
global driver

class MyTest(unittest.TestCase):

	def setUp(self):
		# pass
		Appium()









		"""
		# 新版本
		capabilities = {
			'browserName': '',
			'platformName': 'Android',
			'platformVersion': '7.0',
			'deviceName': '94ea31d1',  # 小米手机
			# 'platformVersion': '6.0',
			# 'deviceName': 'N2F3B61571177075',
			# 'appPackage': 'com.pangpangzhu.p2papp.fengqi',
			# 'appActivity': 'com.pangpangzhu.p2papp.pangpangpig.welcom.WelcomActivity',
			# 'appActivity': 'com.zkbc.p2papp.ui.activity.StartActivity',
			# 'unicodeKeyboard': True,
			# 'resetKeyboard': True,
			'noReset': True
			# 'noReset': False
			}
		"""

		# self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)

	def tearDown(self):
		Appium.driver.quit()


if __name__ == '__main__':
	unittest.main()

