# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep
from zhanghu.shezhi import Shezhi


class TixianPage(Shezhi):
	# 提现
	tixian_text = (By.XPATH, "//android.widget.TextView[@text='提现']")
	# 到账银行
	daozhangyinhang_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvAccountBank")
	# 银行卡号
	yinhangkahao_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvUnionPayCode")
	# 可提现金额
	ketixianjine_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvCanWidthdrawRate")
	# 输入提现金额
	shurutixianjine_text = (By.XPATH, "//android.widget.EditText[@text='请输入提现金额']")
	# 快速提现
	kuaisutixian_text = (By.XPATH, "//android.widget.TextView[@text='快速提现']")
	# 大额提现
	daetixian_text = (By.XPATH, "//android.widget.TextView[@text='大额提现']")
	# 确定提现
	quedingtixian_text = (By.XPATH, "//android.widget.TextView[@text='确定提现']")
	# 输入交易密码
	shurujiaoyimima_text = (By.XPATH, "//android.widget.EditText[@content-desc='请输入交易密码']")

	# 提现
	def tixian(self):
		self.driver.find_element(*self.tixian_text).click()
	# 提现金额
	def shurutixianjine(self, text):
		self.driver.find_element(*self.shurutixianjine_text).send_keys(text)
	# 确定提现
	def quedingtixian(self):
		self.driver.find_element(*self.quedingtixian_text).click()

	# 输入交易密码
	def shurujiaoyimima(self, text):
		self.driver.find_element(*self.shurujiaoyimima_text).send_keys(text)


	# 提现
	def tixian_Action(self, tixianjine, jiaoyimima):
		self.tixian()
		self.shurutixianjine(tixianjine)
		self.shurujiaoyimima(jiaoyimima)
		sleep(5)
		self.swipe_up(1000)
		sleep(3)
		self.quedingtixian()