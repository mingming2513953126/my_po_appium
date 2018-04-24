# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from yaoqinghaoyou.yaoqingyouli import Yaoqingyouli
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Yijihaoyou(Yaoqingyouli):
	# 二级好友
	yijihaoyou_text = (By.XPATH, "//android.widget.TextView[@text='一级好友']")
	# 全部二级好友
	quanbuerjihaoyou_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvFriendsNumber")
	# 投资中二级好友
	touzizhongerjihaoyou_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvFriendsInvestmentNum")
	# 未投资二级好友
	weitouzierjihaoyou_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvNoInvestNum")
	# 一级好友
	eryijihaoyou_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvMobile")
	# 二级好友数量
	erjihaoyoushuliang_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvFriendsNumber")
	# 佣金总额
	yongjinzonge_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvFriendsCommission")

