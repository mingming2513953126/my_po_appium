# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from PO.BasePage import Page
from appium import webdriver
from time import sleep
# from base import Base

# driver = webdriver.Remote('http://localhost:4723/wd/hub', Page.capabilities)

class LoginPage(Page):
    # 立即体验
    # experience_immediately_text = (By.XPATH, "com.pangpangzhu.p2papp:id/btn_splash3_start")
    experience_immediately_text = (By.XPATH, "//android.widget.Button[@text='立即体验']")
    # 手机号一键登录
    # login_button_text = (By.XPATH, "//android.widget.Button[@text='手机号一键登录']")
    cellphone_login_button_text = (By.ID, "com.pangpangzhu.p2papp:id/login_btn")
    # 用户名
    login_username_text = (By.ID, "com.pangpangzhu.p2papp:id/et_username")
    # 密码
    login_password_text = (By.ID, "com.pangpangzhu.p2papp:id/et_pass")
    # 登录
    login_button_text = (By.ID, "com.pangpangzhu.p2papp:id/btn_login")
    # 账户
    my_accont_text = (By.ID, "com.pangpangzhu.p2papp:id/rb_4")

    # 立即体验
    def experience_immediately_button(self):
        self.driver.find_element(*self.experience_immediately_text).click()

    # 手机号一键登录
    def cellphone_Login_Button(self):
        self.driver.find_element(*self.cellphone_login_button_text).click()

    # 输入用户名
    def login_Username(self, text):
        self.driver.find_element(*self.login_username_text).send_keys(text)
    # 输入密码
    def login_Pssword(self, text):
        self.driver.find_element(*self.login_password_text).send_keys(text)
    # 登录
    def login_Button(self):
        self.driver.find_element(*self.login_button_text).click()
    # 账户
    def my_accont(self):
        self.driver.find_element(*self.my_accont_text).click()

    # 立即体验--手机号一键登录--用户名，密码
    def login1_Action(self, username, password):
        self.experience_immediately_button()
        sleep(2)
        self.cellphone_Login_Button()
        # sleep(3)
        self.login_Username(username)
        # sleep(1)
        self.login_Pssword(password)
        # sleep(1)
        self.login_Button()

    def login2_Action(self, username, password):
        self.my_accont()
        # sleep(3)
        self.login_Username(username)
        # sleep(1)
        self.login_Pssword(password)
        # sleep(1)
        self.login_Button()



