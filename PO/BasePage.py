# -*- coding: UTF-8 -*-
import os
import time
from appium import webdriver


# 基本层
class Page(object):

    # 初始化
    def __init__(self, appium_driver):
        self.driver = appium_driver

    """
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    
    # 向左滑动

    def swipeLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 向右滑动

    def swipeRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)
    # 重写元素定位的方法
    def find_element(self, loc):
        try:
            return self.driver.find_element_by_id(loc)
        except Exception as e:
            print("未找到%s" % (self, loc))

    """
    def swipe_Down(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

    def swipe_Up(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

    def swipe_Left(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

    def swipe_Rigth(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

    """
    # 重写元素定位的方法
    def find_element(self, loc):
        try:
            return self.driver.find_element_by_id(loc)
        except Exception as e:
            print("未找到%s" % (self, loc))
    """