# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep

from zhanghu.shezhi import Shezhi


class TuichuPage(Shezhi):
	# 退出登录
	tuichudenglu_text = (By.XPATH, "//android.widget.TextView[@text='退出登录']")
	# 确定
	quedingtuichu_text = (By.XPATH, "//android.widget.Button[@text='确定']")
	# 退出登录
	def tuichudenglu(self):
		self.driver.find_element(*self.tuichudenglu_text).click()
	# 确定
	def tuichudenglu_queding(self):
			self.driver.find_element(*self.quedingtuichu_text).click()

	@exe_deco
	# 退出登录
	def tuichudenglu_Action(self):
		self.zhanghu()
		self.shezhi()
		self.swipe_up(1000)
		# self.swipeDown(100)
		self.tuichudenglu()
		self.tuichudenglu_queding()


	def tuichu_Action(self):
		self.input_by_xpath("//android.widget.TextView[@text='账户']")
		self.input_by_id("com.pangpangzhu.p2papp.test:id/ivSetting")
		self.input_by_xpath("//android.widget.TextView[@text='退出登录']")


