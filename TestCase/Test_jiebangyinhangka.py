# -*- coding: utf-8 -*-
# from time import sleep
import unittest
from time import sleep
from Public import myunit
from shouye.home_page import Home_page
from zhanghu.account.bangka import Bangka
from zhanghu.account.shiming import Shiming
from zhanghu.login_page import LoginPage
from zhanghu.account.zhuce import Zhucepage
from zhanghu.account.shezhijiaoyimima import Shezhijiaoyimima

class JiebangyinhangkaTest(myunit.MyTest):
	def test_jiebangyinhangka(self):
		u'''解绑银行卡'''
		popage = LoginPage()
		popage.login('15895809813', '111111')
		pojiebangka = Bangka()
		pojiebangka.jiebangka_Action()




if __name__ == "__main__":
	unittest.main()