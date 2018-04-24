# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Jiaoyimingxi(LoginPage):
	# 交易明细
	jiaoyimingxi_text = (By.XPATH, "//android.widget.TextView[@text='交易明细']")
	# 筛选
	choukuanzhong_text = (By.XPATH, "//android.widget.ImageView[@index='0']")
	# 一个月
	yigeyue_text = (By.XPATH, "//android.widget.TextView[@text='1个月']")
	# 两个月
	lianggeyue_text = (By.XPATH, "//android.widget.TextView[@text='2个月']")
	# 三个月
	sangeyue_text = (By.XPATH, "//android.widget.TextView[@text='3个月']")
	# 三个月以上
	sangeyueyishang_text = (By.XPATH, "//android.widget.TextView[@text='3个月以上']")
	# 投标
	toubiao_text = (By.XPATH, "//android.widget.TextView[@text='投标']")
	# 回收本金
	huishoubenjin_text = (By.XPATH, "//android.widget.TextView[@text='回收本金']")
	# 回收利息
	huishoulixi_text = (By.XPATH, "//android.widget.TextView[@text='回收利息']")
	# 借款成功
	jiekuanchenggong_text = (By.XPATH, "//android.widget.TextView[@text='借款成功']")
	# 借款手续费
	jiekuanshouxufei_text = (By.XPATH, "//android.widget.TextView[@text='借款手续费']")
	# 风险保证金
	fengxianbaozhengjin_text = (By.XPATH, "//android.widget.TextView[@text='风险保证金']")
	# 偿还本息
	changhuanbenxi_text = (By.XPATH, "//android.widget.TextView[@text='偿还本息']")
	# 充值
	chongzhi_text = (By.XPATH, "//android.widget.TextView[@text='充值']")
	# '提现
	tixian_text = (By.XPATH, "//android.widget.TextView[@text=''提现']")
	# 债权转让手续费
	zhaiquanzhuanrangshouxufei_text = (By.XPATH, "//android.widget.TextView[@text='债权转让手续费']")
	# 借款逾期罚息
	jiekuanyuqifaxi_text = (By.XPATH, "//android.widget.TextView[@text='借款逾期罚息']")
	# 借款逾期滞纳金
	jiekuanyuqizhinajin_text = (By.XPATH, "//android.widget.TextView[@text='借款逾期滞纳金']")
	# 收到逾期罚息
	shoudaoyuqifaxi_text = (By.XPATH, "//android.widget.TextView[@text='收到逾期罚息']")
	# 流标
	liubiao_text = (By.XPATH, "//android.widget.TextView[@text='流标']")
	# 完成
	wancheng_text = (By.XPATH, "//android.widget.TextView[@text='完成']")
	# 重置
	chongzhijiaoyimingxi_text = (By.XPATH, "//android.widget.TextView[@text='重置']")
