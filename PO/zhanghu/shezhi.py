# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep
class Shezhi(LoginPage):
	# 手势密码
	shoushimima_text = (By.XPATH, "//android.widget.CompoundButton[@index='2']")
	# 手机认证
	shoujirenzheng_text = (By.XPATH, "//android.widget.TextView[@text='13011111101']")
	# 身份认证
	shenfenrenzheng_text = (By.XPATH, "//android.widget.TextView[@text='已认证']")
	# 江西银行
	jiangxiyinhang_text = (By.XPATH, "//android.widget.TextView[@text='已开户']")
	# 绑定银行卡
	bangdingyinhangka_text = (By.XPATH, "//android.widget.TextView[@text='已绑卡']")
	# 登录密码设置
	denglumimashezhi_text = (By.XPATH, "//android.widget.TextView[@text='登录密码设置']")
	# 交易密码
	jiaoyimima_text = (By.XPATH, "//android.widget.TextView[@text='重置交易密码']")
	# 更改第三方手机号
	genggaisanfangshoujihao_text = (By.XPATH, "//android.widget.TextView[@text='更改第三方手机号']")
	# 在线反馈
	zaixianfankui_text = (By.XPATH, "//android.widget.TextView[@text='在线反馈']")
	# 客服电话
	kefudianhua_text = (By.XPATH, "//android.widget.TextView[@text='客服电话']")
	# 当前版本
	dangqianbanben_text = (By.XPATH, "//android.widget.TextView[@text='当前版本']")
	# 退出登录
	tuichudenglu_text = (By.XPATH, "//android.widget.TextView[@text='退出登录']")