 # -*- coding: utf-8 -*-
# from time import sleep
import unittest
 from time import sleep
from shouye.home_page import Home_page

 from Public import myunit
 import unittest
 from time import sleep

 from Public import myunit
 from shouye.home_page import Home_page


 class HomePage(myunit.MyTest):
	def test_Home_page(self):
		u'''首页'''
		pohome_page = Home_page()
		sleep(6)
		pohome_page.home_page()
		sleep(2)
		pohome_page.risk_audits()
		# pohome_page.home_risk()
		sleep(6)



if __name__ == "__main__":
	unittest.main()