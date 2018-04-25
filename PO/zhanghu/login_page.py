
# -*- coding: utf-8 -*-
from tool.deco import exe_deco
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from tool.driver import Appium
from appium import webdriver
from time import sleep


# driver = webdriver.Remote('http://localhost:4723/wd/hub', Page.capabilities)

class LoginPage(Appium):
    # 手机号
    cellphone_number_text = (By.XPATH, "//android.widget.EditText[@text='手机号']")
    # 密码
    login_password_text = (By.ID, "com.pangpangzhu.p2papp.test:id/etLoginPass")
    # 登录
    login_button_text = (By.XPATH, "//android.widget.TextView[@text='登录']")
    # 注册
    login_register_text = (By.XPATH, "//android.widget.TextView[@text='注册']")
    # 忘记密码
    forget_password_text = (By.XPATH, "//android.widget.TextView[@text='注册']")
    # 手机号
    def cellphone_number(self, text):
        self.driver.find_element(*self.cellphone_number_text).send_keys(text)
    # 密码
    def login_password(self, text):
        self.driver.find_element(*self.login_password_text).send_keys(text)
    # 登录按钮
    def login_button(self):
        self.driver.find_element(*self.login_button_text).click()
    # 注册
    def login_register(self):
        self.driver.find_element(*self.login_register_text).click()
    # 忘记密码
    def forget_password(self):
        self.driver.find_element(*self.forget_password_text).click()


    # 用户名-密码-登录
    def usr_pwd_button(self, usr, pwd):
        self.cellphone_number(usr)
        self.login_password(pwd)
        self.login_button()
        # sleep(1)

    # 去注册
    def go_register_Action(self):
        self.login_register()

    # 忘记密码
    def forget_pwd(self):
        self.forget_password()

    # 登录
    @exe_deco
    def login(self, usr, pwd):
        # xpath
        self.input_by_xpath("//android.widget.EditText[@text='手机号']", usr)
        self.input_by_id("com.pangpangzhu.p2papp.test:id/etLoginPass", pwd)
        # self.click_by_xpath("//android.widget.TextView[@text='登录']")
        self.click_by_id("com.pangpangzhu.p2papp.test:id/tvDoLogin")
        # id
        # self.input_by_id("com.pangpangzhu.p2papp.fulu: id / etLoginName", usr)
        # self.input_by_id("com.pangpangzhu.p2papp.fulu: id / etLoginPass", pwd)
        # self.click_by_id("com.pangpangzhu.p2papp.fulu: id / tvDoLogin")
