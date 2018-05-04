# -*- coding: utf-8 -*-
# from time import sleep
import unittest
from time import sleep
from Public import myunit
from shouye.home_page import Home_page
from zhanghu.account.bangka import Bangka
from zhanghu.account.genggaisanfangshoujihao import Genggaisanfangshoujihao
from zhanghu.account.shiming import Shiming
from zhanghu.login_page import LoginPage
from zhanghu.account.zhuce import Zhucepage
from zhanghu.account.shezhijiaoyimima import Shezhijiaoyimima

class GenggaisanfangshoujihaoTest(myunit.MyTest):
	def test_genggaisanfangshoujihao(self):
		u'''更改三方手机号'''
		popage = LoginPage()
		username = '15895809813'
		popage.login(username, '111111')
		pogenggaisanfangshoujihao = Genggaisanfangshoujihao()
		pogenggaisanfangshoujihao.genggaisanfangshoujihao_Action(username, '111111')




if __name__ == "__main__":
	unittest.main()