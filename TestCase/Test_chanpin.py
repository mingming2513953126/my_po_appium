# -*- coding: utf-8 -*-
# from time import sleep
import unittest
from time import sleep
from Public import myunit
from shouye.home_page import Home_page
from zhanghu.login_page import LoginPage
from PO.chanpin.product_page import ChanpinPage

class ChanpinTest(myunit.MyTest):
	def test_chanpin(self):
		u'''产品'''
		pochanpin = ChanpinPage()
		# sleep(7)
		pochanpin.chanpin_Action()

		sleep(5)




if __name__ == "__main__":
	unittest.main()