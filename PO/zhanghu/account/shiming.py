# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Shiming(LoginPage):
	# 立即开通弹窗
	lijikaitongtanchuang_text = (By.XPATH, "//android.widget.TextView[@text='立即开通']")
	# 真实姓名
	zhenshixingming_text = (By.XPATH, "//android.widget.EditText[@text='请输入您的姓名']")
	# 身份证号
	shenfenzhenghao_text = (By.XPATH, "//android.widget.EditText[@text='身份证号']")
	# 银行卡号
	yinhangkahao_text = (By.XPATH, "//android.widget.EditText[@text='银行卡号']")
	# 手机号
	shoujihao_text = (By.XPATH, "//android.widget.EditText[@text='手机号']")
	# 阅读并同意
	yuedubingtongyi_text = (By.XPATH, "//android.widget.CheckBox[@text='阅读并同意']")
	# 立即开通
	lijikaitong_text = (By.XPATH, "//android.widget.TextView[@text='立即开通']")


	# 立即开通弹窗
	def lijikaitongtanchuang(self):
		self.driver.find_element(*self.lijikaitongtanchuang_text).click()
	# 真实姓名
	def zhenshixingming(self, text):
		self.driver.find_element(*self.zhenshixingming_text).send_keys(text)
	# 身份证号
	def shenfenzhenghao(self, text):
		self.driver.find_element(*self.shenfenzhenghao_text).send_keys(text)
	# 银行卡号
	def yinhangkahao(self, text):
		self.driver.find_element(*self.yinhangkahao_text).send_keys(text)
	# 手机号
	def shoujihao(self, text):
		self.driver.find_element(*self.shoujihao_text).send_keys(text)
	# 阅读并同意
	def yuedubingtongyi(self):
		self.driver.find_element(*self.yuedubingtongyi_text).click()
	# 立即开通
	def lijikaitong(self):
		self.driver.find_element(*self.lijikaitong_text).click()

	@exe_deco
	# 实名
	def shiming_Action(self, zhenshixingming, shenfenzhenghao, yinhangkahao, shojihao):
		self.lijikaitongtanchuang()
		self.zhenshixingming(zhenshixingming)
		self.shenfenzhenghao(shenfenzhenghao)
		self.yinhangkahao(yinhangkahao)
		self.shoujihao(shojihao)
		self.yuedubingtongyi()
		self.lijikaitong()


