# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from tool.driver import Appium

class Fengxianzicha(Appium):
	# 重新测试
	chongxinceshi_text = (By.XPATH, "//android.widget.TextView[@text='重新测试']")
	# 确定
	enterfengxianceping_text = (By.XPATH, "//android.widget.TextView[@text='确定']")
	# 年龄
	nianling_text = (By.XPATH, "//android.widget.RadioButton[@content-desc=' E、50岁以上']")
	# 家庭收入
	jiatingshouru_text = (By.XPATH, "//android.widget.RadioButton[@content-desc=' E、30万以上']")
	# 关注
	guanzhu_text = (By.XPATH, "//android.widget.CheckBox[@content-desc=' B、资金收益']")
	# 回报
	huibao_text = (By.XPATH, "//android.widget.RadioButton[@content-desc=' E、12%以上']")
	# 期限
	qixian_text = (By.XPATH, "//android.widget.RadioButton[@content-desc=' E、12月以上']")
	# 确认提交
	querentijiao_text = (By.XPATH, "//android.view.View[@content-desc='确认提交']")
	# 未填写确定
	weitianxie_text = (By.XPATH, "//android.widget.Button[@text='确定']")

	# 重新测试
	def chongxinceshi(self):
		self.driver.find_element(*self.chongxinceshi_text).click()
	# 确定
	def enterfengxianceping(self):
		self.driver.find_element(*self.enterfengxianceping_text).click()
	# 年龄
	def nianling(self):
		self.driver.find_element(*self.nianling_text).click()
	# 家庭收入
	def jiatingshouru(self):
		self.driver.find_element(*self.jiatingshouru_text).click()
	# 关注
	def guanzhu(self):
		self.driver.find_element(*self.guanzhu_text).click()
	# 回报
	def huibao(self):
		self.driver.find_element(*self.huibao_text).click()
	# 期限
	def qixian(self):
		self.driver.find_element(*self.qixian_text).click()
	# 确认提交
	def querentijiao(self):
		self.driver.find_element(*self.querentijiao_text).click()
	# 未填写确定
	def weitianxie(self):
		self.driver.find_element(*self.weitianxie_text).click()

	def fengxianceping_Action(self):
		self.nianling()
		self.jiatingshouru()
		self.guanzhu()
		self.huibao()
		self.qixian()
		self.querentijiao()