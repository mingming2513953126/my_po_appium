# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep
class Yanjingandyuetongbu(LoginPage):
	# 账号信息
	zhanghaoxinxi_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvUserName")
	# 眼睛
	yanjing_text = (By.XPATH, "//android.widget.CompoundButton[@index='2']")
	# 余额同步
	yuetongbu_text = (By.XPATH, "//android.widget.TextView[@text='13011111101']")
	# 资产总额
	zichanzonge_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvAssetTotals")
	# 代收本金
	daishoubenjin_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvCatipal")
	# 代收利息
	daishoulixi_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvInterest")
	# 累计收益
	leijishouyi_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvTotalMoney")
	# 可用余额
	keyongyue_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvBalance")
