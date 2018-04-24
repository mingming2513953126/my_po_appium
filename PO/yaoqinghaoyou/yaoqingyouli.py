# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Yaoqingyouli(LoginPage):
	# 发现
	faxian_text = (By.XPATH, "//android.widget.TextView[@text='发现']")
	# 邀请有礼
	yaoqingyouli_text = (By.XPATH, "//android.widget.TextView[@text='邀请有礼']")
	# 中字
	zhongzi_text = (By.ID, "com.pangpangzhu.p2papp.test:id/ivIcon")
	# 邀请说明
	yaoqingshuoming_text = (By.ID, "com.pangpangzhu.p2papp.test:id/ivQuestion")
	# 代收佣金
	daishouyongjin_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvCollectCommission")
	# 昨日赚得
	zuorizhuande_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvYesterdayCommission")
	# 累计赚得
	leijizhuande_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvTotalCommission")
	# 上月入账
	shangyueruzhang_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvLastMonthCommission")
	# 佣金金额
	yongjinjine_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvAvailableCommission")


