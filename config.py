# coding:utf-8
from os.path import abspath, join, dirname
import logging
import time
import os

ROOT_PATH = dirname(__file__)
DATA_PATH = join(ROOT_PATH, 'data')
APK_PATH = join(ROOT_PATH, 'apk')
LOG_PATH = join(ROOT_PATH, 'log')

_IMAGE = lambda data_path, img_name: abspath(
    join(data_path, img_name)
)

_APK = lambda apk_path, dir_name, apk_name: abspath(
    join(apk_path, dir_name, apk_name)
)


class AppiumierLogConfig:
    LOG_LEVEL = logging.NOTSET
    LOG_FILE_PATH = join(LOG_PATH, str(time.time()) + 'appiumier.log')
    LOG_MAX_SIZE = 10 * 1024 * 1024
    LOG_BACKUP_COUNT = 5
    FILE_LOG_LEVEL = logging.INFO
    STREAM_LOG_LEVEL = logging.INFO


command_executor = 'http://localhost:4723/wd/hub'

'''
	每次安装新包都需要重新配置：
	apk_name
	app_version
'''
apk_name = 'PangPangPig-release-CS-(4.2.2-1).apk'
email = os.environ.get('TEST_USERNAME')
userid = "87625139116"
pwd = os.environ.get('TEST_PASSWORD')
app_version = "版本V4.2.2-1"
nickname = "runcheck4"

'''
指定了appPackage和AppActivity可以不指定appPackage安装路径
'app':_APK(apk_path=APK_PATH,dir_name='zww',apk_name=apk_name),

启动app后若发生activity的切换则需要设置AppWaitActivity
'''
"""
# 小米手机
desired_caps_zww = {
    'deviceName': '94ea31d1',
    'platformVersion': '7.0',
    'platformName': 'Android',
    'appPackage': 'com.pangpangzhu.p2papp',
    'appActivity': 'com.zkbc.p2papp.ui.activity.StartActivity',
    # 'appWaitActivity': 'com.netease.ldzww.login.activity.LoginEntryActivity',
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True,
}
"""

# 华为手机
"""
desired_caps_zww = {
    'deviceName': '94ea31d1',
    'platformVersion': '7.0',
    'platformName': 'Android',
    'appPackage': 'com.pangpangzhu.p2papp.app.fulu',
    'appActivity': 'com.zkbc.p2papp.ui.activity.StartActivity',
    # 'appWaitActivity': 'com.netease.ldzww.login.activity.LoginEntryActivity',
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True,
    "noReset": True,
}
"""

desired_caps_zww = {'platformName': 'Android',
                    'platformVersion': '7.0',
                    'deviceName': '94ea31d1',
                    'app': 'F:\\work\\update\\apk\\cs\\xbcshj\\a40274172b23f49064e57a9599a8666c.apk',
                    'clearSystemFiles': True,
                    'appActivity': 'com.pangpangzhu.p2papp.pangpangpig.welcom.WelcomActivity',
                    'appPackage':'com.pangpangzhu.p2papp.test',
                    # 'automationName': 'UIAutomator2',
                    'noSign': True,
                    'noReset': True
                    }