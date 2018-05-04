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
	# 解班银行卡
	jiebangyinhangka_text = (By.XPATH, "//android.widget.TextView[@text='解绑银行卡']")
	# 银行卡号
	yinhangkahao_text = (By.XPATH, "//android.widget.EditText[@text='请输入您的银行卡号']")
	# 立即绑定
	lijibangding_text = (By.XPATH, "//android.widget.EditText[@text='立即绑定']")
	# 请输入银行卡号
	qingshuruyinhangkahao_text = (By.XPATH, "//android.widget.EditText[@content-desc='请输入绑定银行卡号']")
	# 获取验证码
	huoquyanzhengma_text = (By.XPATH, "//android.view.View[@content-desc='获取验证码']")
	# 输入验证码
	shuruyanzhengma_text = (By.XPATH, "")
	# 输入交易密码
	shurujiaoyimima_text = (By.XPATH, "//android.widget.EditText[@content-desc='请输入交易密码']")
	# 确定绑卡
	quedingbangka_text = (By.XPATH, "")
	# 确定解绑卡
	quedingjiebangka_text = (By.XPATH, "//android.widget.Button[@text='确定']")

	# 绑定银行卡
	def bangdingyinhangka(self):
		self.driver.find_element(*self.bangdingyinhangka_text).click()
	# 解绑银行卡
	def jiebangyinhangka(self):
		self.driver.find_element(*self.jiebangyinhangka_text).click()
	# 银行卡号
	def yinhangkahao(self, text):
		self.driver.find_element(*self.yinhangkahao_text).send_keys(text)
	# 立即绑定
	def lijibangding(self):
		self.driver.find_element(*self.lijibangding_text).click()
	# 请输入银行卡号
	def qingshuruyinhangkahao(self, text):
		self.driver.find_element(*self.qingshuruyinhangkahao_text).send_keys(text)
	# 获取验证码
	def huoquyanzhengma(self):
		self.driver.find_element(*self.huoquyanzhengma_text).click()
	# 输入验证码
	def shuruyanzhengma(self):
		self.driver.find_element(*self.shuruyanzhengma_text).click()
	# 确定绑卡
	def quedingbangka(self):
		self.driver.find_element(*self.quedingbangka_text).click()
	# 请输入交易密码
	def shurujiaoyimima(self, text):
		self.driver.find_element(*self.shurujiaoyimima_text).send_keys(text)
	# 确定解绑卡
	def quedingjiebangka(self):
		self.driver.find_element(*self.quedingjiebangka_text).click()




	# 绑卡
	def bangka_Action(self, yinhangkahao, qingshuruyinhangkahao, jiaoyimima):
		self.zhanghu()
		self.shezhi()
		self.bangdingyinhangka()
		self.yinhangkahao(yinhangkahao)
		self.qingshuruyinhangkahao(qingshuruyinhangkahao)
		self.huoquyanzhengma()
		sleep(3)                                          # 输入交易密码时间
		self.shurujiaoyimima(jiaoyimima)
		self.swipe_up()
		self.quedingbangka()


	# 解绑卡
	def jiebangka_Action(self):
		self.zhanghu()
		self.shezhi()
		self.bangdingyinhangka()
		self.jiebangyinhangka()
		self.quedingjiebangka()