# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from tool.driver import Appium
from PO.BasePage import Page
from appium import webdriver
from time import sleep
# from base import Base


# class Home_page(Page):
class Home_page(Appium):
    # 首页
    home_page_text = (By.XPATH, "//android.widget.TextView[@text='首页']")
    # 账户
    my_accont_text = (By.XPATH, "//android.widget.TextView[@text='账户']")
    # 产品
    produce_text = (By.XPATH, "//android.widget.TextView[@text='产品']")
    # 发现
    discover_text = (By.XPATH, "//android.widget.TextView[@text='发现']")
    # 消息中心
    message_center_text = (By.XPATH, "//android.widget.ImageView[@index='0']")
    # 客户服务
    customer_service_text = (By.XPATH, "//android.widget.ImageView[@index='0']")
    # 风险自查
    risk_audits_text = (By.XPATH, "//android.widget.TextView[@text='风险自查']")
    # 邀请有礼
    get_reward_for_inviting_others_text = (By.XPATH, "//android.widget.TextView[@text='邀请有礼']")
    # 信息披露
    information_disclosure_text = (By.ID, "//android.widget.TextView[@text='信息披露']")
    # 每日签到
    daily_attendance_text = (By.ID, "//android.widget.TextView[@text='每日签到']")
    # 立即注册
    register_immediately_text = (By.ID, "//android.widget.TextView[@text='立即注册']")


    # 首页
    def home_page(self):
        self.driver.find_element(*self.home_page_text).click()
    # 账户
    def my_accont(self):
        self.driver.find_element(*self.my_accont_text).click()
    # 产品
    def produce(self):
        self.driver.find_element(*self.produce_text).click()
    # 发现
    def discover(self):
        self.driver.find_element(*self.discover_text).click()
    # 消息中心
    def message_center(self):
        self.driver.find_element(*self.message_center_text).click()
    # 客服服务
    def customer_service(self):
        self.driver.find_element(*self.customer_service_text).click()
    # 风险自查
    def risk_audits(self):
        self.driver.find_element(*self.risk_audits_text).click()

    # 邀请有礼
    def get_reward_for_inviting_others(self, text):
        self.driver.find_element(*self. get_reward_for_inviting_others_text).click()

    # 信息披露
    def information_disclosure(self, text):
        self.driver.find_element(*self.information_disclosure_text).click()
    # 每日签到
    def daily_attendance(self):
        self.driver.find_element(*self.daily_attendance_text ).click()
    # 立即注册
    def register_immediately(self):
        self.driver.find_element(*self.register_immediately_text).click()

    # 首页——账户
    def home_account(self):
        self.my_accont()

    # 我的账户
    def myaccount(self):
        self.click_by_xpath("//android.widget.TextView[@text='账户']")

    def login2_Action(self, username, password):
        self.my_accont()
        # sleep(3)
        self.login_Username(username)
        # sleep(1)
        self.login_Pssword(password)
        # sleep(1)
        self.login_Button()

    def meiriqiandao_Action(self):
        self.click_by_xpath("//android.widget.TextView[@text='首页']")
        self.click_by_xpath("//android.widget.TextView[@text='每日签到']")