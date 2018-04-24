# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep

from zhanghu.shezhi import Shezhi


class Shezhijiaoyimima(Shezhi):
	# 请输入交易密码
	qingshurujiaoyimima_text = (By.XPATH, "//android.widget.EditText[@content-desc='请输入交易密码']")
	# 再次输入交易密码
	zaicishurujiaoyimima_text = (By.XPATH, "//android.widget.EditText[@content-desc='请输入交易密码']")
	# 确定交易密码
	quedingjiaoyimima_text = (By.XPATH, "//android.view.View[@content-desc='确定']")


	# 请输入交易密码
	def qingshurujiaoyimima(self, text):
		self.driver.find_element(*self.qingshurujiaoyimima_text).send_keys(text)
	# 再次输入交易密码
	def zaicishurujiaoyimima(self, text):
		self.driver.find_element(*self.zaicishurujiaoyimima_text).send_keys(text)
	# 确定交易密码
	def quedingjiaoyimima(self):
		self.driver.find_element(*self.quedingjiaoyimima_text).click()

	@exe_deco
	# 设置交易密码
	def shezhijiaoyimima_Action(self, qingshurujiaoyimima, zaicishurujiaoyimima):
		self.zhanghu()
		self.shezhi()
		self.shezhijiaoyimima()
		self.qingshurujiaoyimima(qingshurujiaoyimima)
		self.zaicishurujiaoyimima(zaicishurujiaoyimima)
		self.quedingjiaoyimima()


