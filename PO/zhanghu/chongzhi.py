# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep
from zhanghu.shezhi import Shezhi

class ChongzhiPage(Shezhi):
	# 充值
	chongzhi_text = (By.XPATH, "//android.widget.TextView[@text='充值']")
	# 充值金额
	chongzhijine_text = (By.XPATH, "//android.widget.EditText[@text='请输入充值金额']")
	# 立即充值
	lijichongzhi_text = (By.XPATH, "//android.widget.TextView[@text='立即充值']")
	# 支付宝充值
	zhifubaochongzhi_text = (By.XPATH, "//android.widget.TextView[@text='支付宝充值']")
	# 银行转账
	yinhangzhuanzhang_text = (By.XPATH, "//android.widget.TextView[@text='银行转账']")
	# 温馨提示
	wenxintishi_text = (By.CLASS_NAME, "android.widget.TextView")




	# 获取验证码点击事件
	huoquyanzhengma_button_text = (By.XPATH, "//android.view.View[@content-desc='获取验证码']")
	# 验证码
	yanzhengma_text = (By.XPATH, "//android.widget.EditText[@content-desc='请输入验证码']")
	# 输入交易密码
	shurujiaoyimima_text = (By.XPATH, "//android.widget.EditText[@content-desc='请输入交易密码']")
	# 确定充值
	querenchongzhi_button_text = (By.XPATH, "//android.view.View[@content-desc='确定']")


	# 支付宝充值
	# 收款方姓名
	shoukuanfangxingming_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvTransName")
	# 收款方账号
	shoukuanfangzhanghao_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvZfbNum")
	# 复制前往支付宝
	fuzhiqianwangzhifubao_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvZfbCopy")
	# 收款银行
	shoukuanyinhang_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvAccountBank")


	# 银行转账
	# 收款方姓名
	kaihudi_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvAccountPlace")
	# 开户分行
	kaihufenhang_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvAccountBankBranch")

	# 充值
	def chongzhi(self):
		self.driver.find_element(*self.chongzhi_text).click()
	# 充值金额
	def chongzhijine(self, text):
		self.driver.find_element(*self.chongzhijine_text).send_keys(text)
	# 立即充值
	def lijichongzhi(self):
		self.driver.find_element(*self.lijichongzhi_text).click()
	# 获取验证码点击事件
	def huoquyanzhengma_button(self):
		self.driver.find_element(*self.huoquyanzhengma_button_text).click()
	# 验证码
	def yanzhengma(self, text):
		self.driver.find_element(*self.yanzhengma_text).send_keys(text)
	# 输入交易密码
	def shurujiaoyimima(self, text):
		self.driver.find_element(*self.shurujiaoyimima_text).send_keys(text)
	# 缺人充值
	def querenchongzhi_button(self):
		self.driver.find_element(*self.querenchongzhi_button_text).click()

	# 充值
	def chongzhi_Action(self, chongzhijine, jiaoyimima):
		self.zhanghu()
		self.chongzhi()
		self.chongzhijine(chongzhijine)
		self.lijichongzhi()
		sleep(5)
		self.swipe_up(1000)
		sleep(3)
		self.huoquyanzhengma_button()
		# self.yanzhengma(yanzhengma)
		sleep(5)
		self.shurujiaoyimima(jiaoyimima)
		self.querenchongzhi_button()
