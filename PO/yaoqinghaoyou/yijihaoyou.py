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
	# 一级好友
	yijihaoyou_text = (By.XPATH, "//android.widget.TextView[@text='一级好友']")
	# 全部一级好友
	quanbuyijihaoyou_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvFriendsNumber")
	# 投资中一级好友
	touzizhongyijihaoyou_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvFriendsInvestmentNum")
	# 未投资一级好友
	weitouziyijihaoyou_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvNoInvestNum")
	# 全部
	quanbu_text = (By.XPATH, "//android.widget.TextView[@text='全部']")
	# 投资中
	touzizhong_text = (By.XPATH, "//android.widget.TextView[@text='投资中']")
	# 未投资
	weitouzi_text = (By.XPATH, "//android.widget.TextView[@text='未投资']")

