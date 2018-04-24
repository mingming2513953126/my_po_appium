# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Zhucepage(LoginPage):
	# 请输入手机号
	qingshurushoujihao_text = (By.XPATH, "//android.widget.EditText[@text='请输入手机号']")
	# 设置密码
	# shezhimima_text = (By.XPATH, "//android.widget.EditText[@index='1']")
	shezhimima_text = (By.ID, "com.pangpangzhu.p2papp.test:id/etRegisterPass")
	# 获取验证码
	huoquyanzhengma_text = (By.XPATH, "//android.widget.TextView[@text='获取验证码']")
	# 验证码
	yanzhengma_text = (By.XPATH, "//android.widget.EditText[@text='验证码']")
	# 邀请码
	yaoqingma_text = (By.XPATH, "//android.widget.EditText[@text='邀请码，没有可不填写']")
	# 注册按钮
	zhuce_text = (By.XPATH, "//android.widget.TextView[@text='注册']")

	# 手机号
	def shoujihao(self, text):
		self.driver.find_element(*self.qingshurushoujihao_text).send_keys(text)

	# 设置密码
	def shezhimima(self, text):
		self.driver.find_element(*self.shezhimima_text).send_keys(text)

	# 获取验证码
	def huoquyanzhengma(self):
		self.driver.find_element(*self.huoquyanzhengma_text).click()

	# 验证码
	def yanzhengma(self, text):
		self.driver.find_element(*self.yanzhengma_text).send_keys(text)

	# 验证码
	def yaoqingma(self, text):
		self.driver.find_element(*self.yaoqingma_text).send_keys(text)

	# 注册
	def zhuce(self):
		self.driver.find_element(*self.zhuce_text).click()

	@exe_deco
	# 注册
	def zhuce_Action(self, shoujihao, mima, yanzhengma):
		self.shoujihao(shoujihao)
		self.shezhimima(mima)
		self.huoquyanzhengma()
		self.yanzhengma(yanzhengma)
		self.zhuce()

