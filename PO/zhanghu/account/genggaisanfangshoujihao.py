# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep

from zhanghu.shezhi import Shezhi


class Genggaisanfangshoujihao(Shezhi):
	# 新手机号
	xinshoujihao_text = (By.XPATH, "//android.widget.EditText[@text='请输入您的新手机号']")
	# 获取验证码
	huoquyanzhengma_text = (By.XPATH, "//android.widget.TextView[@text='获取验证码']")
	# 输入验证码
	shuruyanzhengma_text = (By.XPATH, "//android.widget.EditText[@text='请输入您的验证码']")
	# 立即修改
	lijixiugai_text = (By.XPATH, "//android.widget.TextView[@text='立即修改']")
	# 修改成功
	xiugaichenggong_text = (By.XPATH, "")

	# 新手机号
	def xinshoujihao(self, text):
		self.driver.find_element(*self.xinshoujihao_text).send_keys(text)
	# 获取验证码
	def huoquyanzhengma(self):
		self.driver.find_element(*self.huoquyanzhengma_text).click()
	# 输入验证码
	def shuruyanzhengma(self, text):
		self.driver.find_element(*self.shuruyanzhengma_text).send_keys(text)
	# 立即修改
	def lijixiugai(self):
		self.driver.find_element(*self.lijixiugai_text).click()




	# 更改三方手机号
	def genggaisanfangshoujihao_Action(self, xinshoujihao, yanzhengma):
		self.zhanghu()
		self.shezhi()
		self.genggaidisanfangshoujihao()
		self.xinshoujihao(xinshoujihao)
		self.huoquyanzhengma()
		self.shuruyanzhengma(yanzhengma)
		self.lijixiugai()


