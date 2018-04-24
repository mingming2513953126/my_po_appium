# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Chanpin(LoginPage):
	# 产品
	chanpinsanbiao_text = (By.XPATH, "//android.widget.TextView[@text='产品']")
	# 债权
	chanpinzhaiquan_text = (By.XPATH, "//android.widget.TextView[@text='债权']")
	# 产品详情-马上投资
	mashangtouzi_text = (By.XPATH, "//android.widget.TextView[@text='马上投资']")
	# 购买金额
	goumaijine_text = (By.XPATH, "//android.widget.EditText[@text='100元起投，且以一百元整数倍递增']")
	# 余额全投
	guizeshuoming_text = (By.XPATH, "//android.widget.TextView[@text='余额全投']")
	# 使用优惠券
	shiyongyouhuiquan_text = (By.XPATH, "//android.widget.TextView[@text='使用优惠券']")
	# 卡券第一个
	kaquandiyige_text = (By.XPATH, "//android.widget.CheckBox[@index='2']")




	
	# 出借期限
	chujieqixian_text = (By.XPATH, "//android.widget.TextView[@text='出借期限']")
	# 还款方式
	huankuanfangshi_text = (By.XPATH, "//android.widget.TextView[@text='还款方式']")
	# 出借金额低
	chujiejinedi_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvSumFloor")
	# 出借金额高
	chujiejinegao_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvSumCeil")
	# 使用优惠券
	shiyongyouhuiquan_text = (By.ID, "com.pangpangzhu.p2papp.test:id/sbSwitch")
	# 我已阅读并同意三个协议
	zidongtoubiaosangexieyi_text = (By.XPATH, "//android.widget.CheckBox[@text='我已阅读并同意']")
	# 风险提示确认函
	fengxiantishiquerenhan_text = (By.XPATH, "//android.widget.TextView[@text='《风险提示确认函》']")
	# 风险提示书
	fengxiantishishu_text = (By.XPATH, "//android.widget.TextView[@text='《风险提示书》']")
	# 借贷项目说明书
	jiedaixiangmushuomingshu_text = (By.XPATH, "//android.widget.TextView[@text='《借贷项目说明书》']")
	# 保存设置
	baocunzidongtoubiaoshezhi_text = (By.XPATH, "//android.widget.Button[@text='保存设置']")
	# 暂不修改
	zanbuxiugaizidongtoubiaoshezhi_text = (By.XPATH, "//android.widget.Button[@text='暂不修改']")
	# 返回
	fanhuizidongtoubiaoshezhi_text = (By.XPATH, "//android.widget.ImageView[@index='0']")
