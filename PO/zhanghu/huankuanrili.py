# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Huankuanrili(LoginPage):
	# 还款日历
	huankuanrili_text = (By.XPATH, "//android.widget.TextView[@text='还款日历']")

