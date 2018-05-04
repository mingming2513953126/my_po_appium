# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep

from zhanghu.shezhi import Shezhi


class Bangka(Shezhi):
	# 绑定银行卡
	bangdingyinhangka_text = (By.XPATH, "//android.widget.TextView[@text='绑定银行卡']")
	# 银行卡号
	yinhangkahao_text = (By.XPATH, "")
	# 获取验证码
	huoquyanzhengma_text = (By.XPATH, "")
	# 输入验证码
	shuruyanzhengma_text = (By.XPATH, "")
	# 确定绑卡
	quedingbangka_text = (By.XPATH, "")

	# 绑定银行卡
	def bangdingyinhangka(self):
		self.driver.find_element(*self.bangdingyinhangka_text).click()
	# 银行卡号
	def yinhangkahao(self, text):
		self.driver.find_element(*self.yinhangkahao_text).send_keys(text)
	# 获取验证码
	def huoquyanzhengma(self):
		self.driver.find_element(*self.huoquyanzhengma_text).click()
	# 输入验证码
	def shuruyanzhengma(self):
		self.driver.find_element(*self.shuruyanzhengma_text).click()
	# 确定绑卡
	def quedingbangka(self, text):
		self.driver.find_element(*self.quedingbangka_text).send_keys(text)



	@exe_deco
	# 绑卡
	def bangka_Action(self, qingshurujiaoyimima, zaicishurujiaoyimima):
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

