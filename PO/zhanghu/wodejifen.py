# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Wodejifen(LoginPage):
	# 积分商城
	jifenshangcheng_text = (By.XPATH, "//android.widget.TextView[@text='赚积分、换礼品、抽奖']")
	# 当前积分
	dangqianjifen_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvScore")
	# 全国排名
	quanguopaiming_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvRank")
	# 待领取
	dangqianpaiming_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvReceive")
