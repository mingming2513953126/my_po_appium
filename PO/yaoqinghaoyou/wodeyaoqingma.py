# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from yaoqinghaoyou.yaoqingyouli import Yaoqingyouli
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Wodeyaoqingma(Yaoqingyouli):
	# 邀请码
	yaoqingma_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvMyCode")
	# 二维码
	erweima_text = (By.XPATH, "//android.widget.TextView[@text='二维码']")
	# 保存二维码
	baocunerweima_text = (By.XPATH, "//android.widget.TextView[@text='保存']")
	# 分享二维码
	fenxiangerweima_text = (By.XPATH, "//android.widget.TextView[@text='分享']")
	# 邀请说明
	yaoqingshuoming_text = (By.XPATH, "//android.widget.TextView[@text='邀请说明']")
	# 拷贝邀请码
	kaobeiyaoqingma_text = (By.XPATH, "//android.widget.TextView[@text='拷贝']")
