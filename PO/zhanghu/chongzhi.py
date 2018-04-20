# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep
class Chongzhi(LoginPage):
	# 充值
	chongzhi_text = (By.XPATH, "//android.widget.TextView[@text='充值']")
	# 充值金额
	chongzhijine_text = (By.XPATH, "//android.widget.EditText[@text='请输入充值金额']")
	# 立即充值
	lijichongzhi_text = (By.XPATH, "//android.widget.TextView[@text='立即充值']")
	# 支付宝充值
	zhifubaochongzhi_text = (By.XPATH, "//android.widget.TextView[@text='支付宝充值']")
	# 银行转账
	yinhangzhuanzhang_text = (By.XPATH, "//android.widget.TextView[@text='银行转账']")
	# 温馨提示
	wenxintishi_text = (By.CLASS_NAME, "android.widget.TextView")




	# 获取验证码点击事件
	huoquyanzhengma_button_text = (By.XPATH, "//android.view.View[@content-desc='获取验证码']")
	# 验证码
	yanzhengma_text = (By.XPATH, "//android.widget.EditText[@content-desc='请输入验证码']")
	# 输入交易密码
	shurujiaoyimima_text = (By.XPATH, "//android.widget.EditText[@content-desc='请输入交易密码']")
	# 确定充值
	querenchongzhi_button_text = (By.XPATH, "//android.view.View[@content-desc='确定']")


	# 支付宝充值
	# 收款方姓名
	shoukuanfangxingming_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvTransName")
	# 收款方账号
	shoukuanfangzhanghao_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvZfbNum")
	# 复制前往支付宝
	fuzhiqianwangzhifubao_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvZfbCopy")
	# 收款银行
	shoukuanyinhang_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvAccountBank")


	# 银行转账
	# 收款方姓名
	kaihudi_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvAccountPlace")
	# 开户分行
	kaihufenhang_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvAccountBankBranch")
