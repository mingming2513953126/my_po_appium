# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from tool.driver import Appium

class Xiaoxizhongxin(Appium):
	# 消息中心
	xiaoxizhongxin_text = (By.XPATH, "//android.widget.ImageView[@index='0']")
	def xiaoxizhongxin(self):
		self.driver.find_element(*self.xiaoxizhongxin_text).click()

class xitonggognggao(Appium):
	# 系统公告
	xitonggognggao_text = (By.XPATH, "//android.widget.TextView[@text='系统公告']")
	def xitonggognggao_Action(self):
		self.driver.find_element(*self.xitonggognggao_text).click()

class wodexiaoxi(Appium):
	# 我的消息
	wodexiaoxi_text = (By.XPATH, "//android.widget.TextView[@text='我的消息']")
	def wodexiaoxi_Action(self):
		self.driver.find_element(*self.wodexiaoxi_text).click()

class jingxuanhuodong(Appium):
	# 精选活动
	jingxuanhuodong_text = (By.XPATH, "//android.widget.TextView[@text='精选活动']")
	def jingxuanhuodong_Action(self):
		self.driver.find_element(*self.jingxuanhuodong_text).click()

class pingtaidongtai(Appium):
	# 平台动态
	pingtaidongtai_text = (By.XPATH, "//android.widget.TextView[@text='平台动态']")
	def pingtaidongtai_Action(self):
		self.driver.find_element(*self.pingtaidongtai_text).click()