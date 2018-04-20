# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from tool.driver import Appium
from appium import webdriver
from time import sleep
# from base import Base

# driver = webdriver.Remote('http://localhost:4723/wd/hub', Page.capabilities)

# class LoginPage(Page):
class LoginPage(Appium):
    # 手机号   这些我在定位元素   说白了就是在给变量命名  例子：a=1
    cellphone_number_text = (By.XPATH, "//android.widget.EditText[@text='请输入手机号']")
    # 密码
    login_password_text = (By.XPATH, "//android.widget.EditText[@text='登录密码']")
    # 点击获取验证码
    get_code_button_text = (By.XPATH, "//android.widget.TextView[@text='获取验证码']")
    # 验证码
    code_text = (By.XPATH, "//android.widget.EditText[@text='验证码']")
    # 邀请码
    login_register_text = (By.XPATH, "//android.widget.EditText[@text='邀请码，没有可不填写']")
    # 注册
    register_button_text = (By.XPATH, "//android.widget.TextView[@text='注册']")

    # 登录
    def login(self):
        # 用户名
        self.input_by_xpath()


    # 手机号   这里开始封装函数
    def cellphone_number(self, text):
        self.driver.find_element(*self.cellphone_number_text).send_keys(text)
    # 密码
    def login_password(self, text):
        self.driver.find_element(*self.login_password_text).send_keys(text)
    # 点击获取验证码
    def get_code_button(self):
        self.driver.find_element(*self.get_code_button_text).click()

    # 验证码
    def code(self):
        self.driver.find_element(*self.code_text).send_keys()
    # 注册
    def login_register(self):
        self.driver.find_element(*self.login_register_text).click()
    # 忘记密码
    def forget_password(self):
        self.driver.find_element(*self.forget_password_text).click()


    # 用户名-密码-登录
    def usr_pwd_button(self, username, password):
        self.cellphone_number(username)
        self.login_password(password)
        self.login_button()
        # sleep(1)


    def login2_Action(self, username, password):
        self.my_accont()
        # sleep(3)
        self.login_Username(username)
        # sleep(1)
        self.login_Pssword(password)
        # sleep(1)
        self.login_Button()



