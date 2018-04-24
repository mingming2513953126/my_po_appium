# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from zhanghu.login_page import LoginPage
from tool.driver import Appium
from appium import webdriver
from time import sleep


class Zidongtoubiao(LoginPage):
	# 自动投标设置
	zidongtoubiaoshezhi_text = (By.XPATH, "//android.widget.TextView[@text='设置']")
	# 最低利率
	zuidililv_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvMixInterest")
	# 回款周期
	huikuanzhouqi_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvBackCycle")
	# 当前排名
	dangqianpaiming_text = (By.ID, "com.pangpangzhu.p2papp.test:id/tvRankNow")
	# 规则说明
	guizeshuoming_text = (By.XPATH, "//android.widget.TextView[@text='规则说明']")
	# 自动投标开关
	zidongtoubiaokaiguan_text = (By.XPATH, "//android.widget.CompoundButton[@index='2']")
	# 预期年化利率
	yuqinianhualilv_text = (By.XPATH, "//android.widget.TextView[@text='预期年化利率']")
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
