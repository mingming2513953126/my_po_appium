#!/usr/bin/python
 # -*- coding: utf-8 -*-
# from time import sleep
import unittest
from time import sleep
import xlrd
from Public import myunit
from shouye.home_page import Home_page
from zhanghu.account.tuichu import TuichuPage
from zhanghu.login_page import LoginPage
def open_excel(file= 'file.xlsx'):
	try:
		data = xlrd.open_workbook(file)
		return data
	except BaseException as e:
		print (str(e))  #根据索引获取Excel表格中的数据 参数:file：Excel文件路径 colnameindex：表头列名所在行的所以 ，by_index：表的索引
def excel_table_byindex(file= 'file.xlsx',colnameindex=0,by_index=0):
	data = open_excel(file)
	table = data.sheets()[by_index]
	nrows = table.nrows #行数
	colnames = table.row_values(colnameindex) #某一行数据
	list =[]
	for rownum in range(1,nrows):
		row = table.row_values(rownum)
		if row:
			app = {}
		for i in range(len(colnames)):
				app[colnames[i]] = row[i]
				list.append(app)
		return list


class Login_canshuhuaTest(myunit.MyTest):

	def test_Login_canshuhua(self):
		u'''登录'''
		listdata = excel_table_byindex("E:\\python\\appium\\my_po_appium_xinban\\test_case\\ceshicase.xlsx", 0)
		if (len(listdata) <= 0):
			assert 0, u"Excel数据异常"
		print(len(listdata))
		for i in range(0, len(listdata)):
			pohome = Home_page()
			# sleep(5)
			pohome.myaccount()
			popage = LoginPage()
			# sleep(7)
			# popage.swipe_Rigth()
			# popage.swipe_Rigth()
			# popage.swipe_Rigth()
			# 用for循环控制多次执行一个自定义函数
			# for i in range(1, 3):
			# 	popage.swipeRight()

			# map(lambda x: popage.swipe_Rigth(), range(0, 3))
			# popage.usr_pwd_button('13011111111', '111111')
			# popage.login2_Action('13011111101', '111111')
			popage.login(listdata[i]['username'], listdata[i]['password'])
			pologinout = TuichuPage()
			pologinout.tuichudenglu_Action()
			sleep(10)


if __name__ == "__main__":
	unittest.main()