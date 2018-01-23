# -*- coding: utf-8 -*-
import os
__author__ = 'JennyHui'
import unittest
# from PO import DashPage
# from selenium import webdriver
from appium import webdriver
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
global driver

class MyTest(unittest.TestCase):

	def setUp(self):
		capabilities = {
						'browserName': '',
						'platformName': 'Android',
						# 'platformVersion': '6.0',
						'platformVersion': '7.0',
						# 'deviceName': 'N2F3B61571177075',
						'deviceName': '94ea31d1',                                        # 小米手机
						'appPackage': 'com.pangpangzhu.p2papp',
						# 'appActivity': 'com.zkbc.p2papp.ui.activity.StartActivity',
						# 'unicodeKeyboard': True,
						# 'resetKeyboard': True,
						# 'noReset': True
						# 'noReset': False
						}

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()

