# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep
class Shezhi(LoginPage):
	# 账户
	zhanghu_text = (By.XPATH, "//android.widget.TextView[@text='账户']")
	# 设置
	shezhi_text = (By.ID, "com.pangpangzhu.p2papp.test:id/ivSetting")
	# 手势密码
	shoushimima_text = (By.XPATH, "//android.widget.CompoundButton[@index='2']")
	# 手机认证
	shoujirenzheng_text = (By.XPATH, "//android.widget.TextView[@text='13011111101']")
	# 身份认证
	shenfenrenzheng_text = (By.XPATH, "//android.widget.TextView[@text='已认证']")
	# 江西银行
	jiangxiyinhang_text = (By.XPATH, "//android.widget.TextView[@text='已开户']")
	# 绑定银行卡
	bangdingyinhangka_text = (By.XPATH, "//android.widget.TextView[@text='已绑卡']")
	# 登录密码设置
	denglumimashezhi_text = (By.XPATH, "//android.widget.TextView[@text='登录密码设置']")
	# 设置交易密码
	shezhijiaoyimima_text = (By.XPATH, "//android.widget.TextView[@text='设置交易密码']")
	# 重置交易密码
	chongzhijiaoyimima_text = (By.XPATH, "//android.widget.TextView[@text='重置交易密码']")
	# 更改第三方手机号
	genggaisanfangshoujihao_text = (By.XPATH, "//android.widget.TextView[@text='更改第三方手机号']")
	# 在线反馈
	zaixianfankui_text = (By.XPATH, "//android.widget.TextView[@text='在线反馈']")
	# 客服电话
	kefudianhua_text = (By.XPATH, "//android.widget.TextView[@text='客服电话']")
	# 当前版本
	dangqianbanben_text = (By.XPATH, "//android.widget.TextView[@text='当前版本']")
	# 退出登录
	tuichudenglu_text = (By.XPATH, "//android.widget.TextView[@text='退出登录']")

	# 账户
	def zhanghu(self):
		self.driver.find_element(*self.zhanghu_text).click()
	# 重置交易密码
	def shezhi(self):
		self.driver.find_element(*self.shezhi_text).click()
	# 设置交易密码
	def shezhijiaoyimima(self):
		self.driver.find_element(*self.shezhijiaoyimima_text).click()
	# 重置交易密码
	def chongzhijiaoyimima(self):
		self.driver.find_element(*self.shezhijiaoyimima_text).click()
	# 更改第三方手机号
	def genggaidisanfangshoujihao(self):
		self.driver.find_element(*self.genggaisanfangshoujihao_text).click()