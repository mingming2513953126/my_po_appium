# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from yaoqinghaoyou.yaoqingyouli import Yaoqingyouli
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Quanmincaifuguihuashi(Yaoqingyouli):
	# 全民财富规划师
	quanmincaifuguihuashi_text = (By.XPATH, "//android.widget.TextView[@text='一级好友']")
	# 立即去邀请好友
	lijiyaoqinghaoyou_text = (By.XPATH, "//android.widget.TextView[@text='立即去邀请好友']")
	# 立即邀请好友
	lijiyaoqing_text = (By.XPATH, "//android.widget.TextView[@text='立即邀请']")
