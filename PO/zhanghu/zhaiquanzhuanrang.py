# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Zhaiquanzhuanrang(LoginPage):
	# 还款日历
	zhaiquanzhuanrang_text = (By.XPATH, "//android.widget.TextView[@text='债权转让']")
	# 可转让
	kezhuanrang_text = (By.XPATH, "//android.widget.TextView[@text='可转让']")
	# 转让中
	zhuanranghzong_text = (By.XPATH, "//android.widget.TextView[@text='转让中']")
	# 已转让
	yizhuanrang_text = (By.XPATH, "//android.widget.TextView[@text='已转让']")
	# 已认购
	yirengou_text = (By.XPATH, "//android.widget.TextView[@text='已认购']")

