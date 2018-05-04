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

class BangdingyinhangkaTest(myunit.MyTest):
	def test_bangdingyinhangka(self):
		u'''绑定银行卡'''
		popage = LoginPage()
		popage.login('15895809813', '111111')
		pobangdingyinhangka = Bangka()
		pobangdingyinhangka.bangka_Action()




if __name__ == "__main__":
	unittest.main()