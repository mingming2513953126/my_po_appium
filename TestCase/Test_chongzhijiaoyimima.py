# -*- coding: utf-8 -*-
# from time import sleep
import unittest
from time import sleep
from Public import myunit
from shouye.home_page import Home_page
from zhanghu.account.shiming import Shiming
from zhanghu.login_page import LoginPage
from zhanghu.account.zhuce import Zhucepage
from zhanghu.account.shezhijiaoyimima import Shezhijiaoyimima

class ShezhijiaoyimimaTest(myunit.MyTest):
	def test_shezhijiaoyimima(self):
		u'''设置交易密码'''
		popage = LoginPage()
		popage.login('13011111101', '111111')
		poshezhijiaoyimima = Shezhijiaoyimima()
		poshezhijiaoyimima.chongzhijiaoyimima_Action()




if __name__ == "__main__":
	unittest.main()