# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Tixian(LoginPage):
	# 提现
	tixian_text = (By.XPATH, "//android.widget.TextView[@text='提现']")
	# 到账银行
	daozhangyinhang_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvAccountBank")
	# 银行卡号
	yinhangkahao_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvUnionPayCode")
	# 可提现金额
	ketixianjine_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvCanWidthdrawRate")
	# 输入提现金额
	shurutixianjine_text = (By.XPATH, "//android.widget.EditText[@text='请输入提现金额']")
	# 快速提现
	kuaisutixian_text = (By.XPATH, "//android.widget.TextView[@text='快速提现']")
	# 大额提现
	daetixian_text = (By.XPATH, "//android.widget.TextView[@text='大额提现']")
	# 确定提现
	quedingtixian_text = (By.XPATH, "//android.widget.TextView[@text='确定提现']")

