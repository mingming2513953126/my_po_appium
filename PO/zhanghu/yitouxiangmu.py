# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Yitouxiangmu(LoginPage):
	# 已投项目
	yitouxiangmu_text = (By.XPATH, "//android.widget.TextView[@text='已投项目']")
	# 筹款中
	choukuanzhong_text = (By.XPATH, "//android.widget.TextView[@text='筹款中']")
	# 回款中
	huikuanzhong_text = (By.XPATH, "//android.widget.TextView[@text='回款中']")
	# 已完成
	yiwancheng_text = (By.XPATH, "//android.widget.TextView[@text='已完成']")

	# 项目标题
	xiangmubiaoti_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvObjectName")
	# 出借金额
	chujiejine_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvLoanMoney")
	# 出借期限
	chujieqixian_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvLoanTime")
	# 年化收益
	nianhuashouyi_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvAnnualReturn")


