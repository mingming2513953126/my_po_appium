# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Kaquanbao(LoginPage):
	# 红包
	hongbao_text = (By.XPATH, "//android.widget.TextView[@text='红包']")
	# 加息券
	jiaxiquan_text = (By.XPATH, "//android.widget.TextView[@text='加息券']")
	# 现金券
	xianjinquan_text = (By.XPATH, "//android.widget.TextView[@text='现金券']")
	# 查看详情
	chakanxiangqing_text = (By.XPATH, "//android.widget.TextView[@text='查看详情']")
	# 未使用
	weishiyong_text = (By.XPATH, "//android.widget.TextView[@text='未使用']")
	# 已使用
	yishiyong_text = (By.XPATH, "//android.widget.TextView[@text='已使用']")
	# 已失效
	yishixiao_text = (By.XPATH, "//android.widget.TextView[@text='已失效']")
	# 红包个数
	hongbaogeshu_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvRedEnvelopes")
	# 加息券个数
	jiaxiquangeshu_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvCoupon")
	# 现金券个数
	xianjinquangeshu_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvCashCoupon")



