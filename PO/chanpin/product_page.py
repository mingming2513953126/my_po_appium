# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class ChanpinPage(LoginPage):
	a = "批A普A027"
	# 产品
	chanpinsanbiao_text = (By.XPATH, "//android.widget.TextView[@text='产品']")
	# 债权
	chanpinzhaiquan_text = (By.XPATH, "//android.widget.TextView[@text='债权']")
	# 指定产品
	# zhidingchanpin_text = (By.XPATH, "//android.widget.TextView[@text= %s] %(a)")
	zhidingchanpin_text = (By.XPATH, "// android.widget.TextView[ @ text = '批A普A027']")
	# zhidingchanpin_text = (By.LINK_TEXT, "批A普A027")
	# 产品详情-马上投资
	mashangtouzi_text = (By.XPATH, "//android.widget.TextView[@text='马上投资']")
	# 购买金额
	goumaijine_text = (By.XPATH, "//android.widget.EditText[@text='100元起投，且以一百元整数倍递增']")
	# 余额全投
	guizeshuoming_text = (By.XPATH, "//android.widget.TextView[@text='余额全投']")
	# 使用优惠券
	shiyongyouhuiquan_text = (By.XPATH, "//android.widget.TextView[@text='使用优惠券']")
	# 卡券第一个
	kaquandiyige_text = (By.XPATH, "//android.widget.CheckBox[@index='2']")

	# 产品
	def chanpinsanbiao(self):
		self.driver.find_element(*self.chanpinsanbiao_text).click()

	# 指定标的
	def zhidingchanpin(self):
		self.driver.find_element(*self.zhidingchanpin_text).click()

	def chanpin_Action(self):
		self.chanpinsanbiao()
		self.zhidingchanpin()







