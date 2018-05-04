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
	# 获取验证码按钮
	huoquyanzhengma_text = (By.XPATH, "//android.widget.Button[@content-desc='获取验证码']")
	# 短信验证码
	duanxinyanzhengma_text = (By.XPATH, "//android.widget.EditText[@content-desc='短信校验码']")
	# 确认
	querenchongzhijiaoyimima_text = (By.XPATH, "//android.widget.Button[@content-desc='确认']")

	# 请输入交易密码
	def qingshurujiaoyimima(self, text):
		self.driver.find_element(*self.qingshurujiaoyimima_text).send_keys(text)
	# 再次输入交易密码
	def zaicishurujiaoyimima(self, text):
		self.driver.find_element(*self.zaicishurujiaoyimima_text).send_keys(text)
	# 确定交易密码
	def quedingjiaoyimima(self):
		self.driver.find_element(*self.quedingjiaoyimima_text).click()
	# 获取验证码
	def huoquyanzhengma(self):
		self.driver.find_element(*self.huoquyanzhengma_text).click()
	# 填写验证码
	def duanxinyanzhengma(self, text):
		self.driver.find_element(*self.duanxinyanzhengma_text).send_keys(text)

	# 确认重置交易密码
	def querenchongzhijiaoyimima(self):
		self.driver.find_element(*self.querenchongzhijiaoyimima_text).click()

	@exe_deco
	# 设置交易密码
	def shezhijiaoyimima_Action(self, qingshurujiaoyimima, zaicishurujiaoyimima):
		self.zhanghu()
		self.shezhi()
		self.shezhijiaoyimima()
		self.qingshurujiaoyimima(qingshurujiaoyimima)
		self.zaicishurujiaoyimima(zaicishurujiaoyimima)
		self.quedingjiaoyimima()

	@exe_deco
	def chongzhijiaoyimima_Action(self, duanxinyanzhengma, qingshurujiaoyimima):
		self.zhanghu()
		self.shezhi()
		self.chongzhijiaoyimima()
		sleep(3)                                           # 手动输入验证码
		self.duanxinyanzhengma(duanxinyanzhengma)
		self.querenchongzhijiaoyimima()
		self.qingshurujiaoyimima(qingshurujiaoyimima)
		self.qingshurujiaoyimima(qingshurujiaoyimima)
		self.quedingjiaoyimima()

