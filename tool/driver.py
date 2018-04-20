# coding:utf-8
from selenium.webdriver.support.wait import WebDriverWait
from config import desired_caps_zww, command_executor
from appium import webdriver


def try_to(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e:
            print(str(e))

    return wrapper


class Appium():

    driver = webdriver.Remote(command_executor, desired_caps_zww)
    # 初始化
    # def __init__(self, appium_driver):
    #     self.driver = appium_driver

    @try_to
    def click_by_id(self, ele_id, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_id(ele_id))
        self.driver.find_element_by_id(ele_id).click()

    @try_to
    def input_by_id(self, ele_id, content, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_id(ele_id))
        el = self.driver.find_element_by_id(ele_id)
        el.click()
        el.send_keys(content)

    @try_to
    def click_by_xpath(self, ele_xpath, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_xpath(ele_xpath))
        self.driver.find_element_by_xpath(ele_xpath).click()

    @try_to
    # def input_by_xpath(self, ele_xpath, content, timeout=10):
    def input_by_xpath(self, ele_xpath, content, timeout=1):
        # WebDriverWait(self.driver).until(lambda driver: driver.find_element_by_xpath(ele_xpath))
        WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_xpath(ele_xpath))
        el = self.driver.find_element_by_xpath(ele_xpath)
        el.click()
        el.clear()
        el.send_keys(content)


    @try_to
    def wait_by_xpath(self, ele_xpath, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_xpath(ele_xpath))
        try:
            self.driver.find_element_by_xpath(ele_xpath)
            sig = "OK"
        except Exception as e:
            sig = "FAILED"
        return sig

    @try_to
    def click_by_text(self, text, timeout=10):
        # 针对TextView定位生效
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element_by_xpath("//android.widget.TextView[@text='" + text + "']"))

    @try_to
    def get_text_by_id(self, ele_id, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_id(ele_id))
        text = self.driver.find_element_by_id(ele_id).get_attribute("text")
        return text

    @try_to
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    @try_to
    # 向上滑动
    def swipe_up(self, time):
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)
        self.driver.swipe(x1, y1, x1, y2, time)

    @try_to
    # 向左滑动
    def swipeLeft(self, time):
        l = self.get_size()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.25)
        self.driver.swipe(x1, y1, x2, y1, time)

    @try_to
    # 向右滑动
    def swipeRight(self, time):
        l = self.get_size()
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, time)

    @try_to
    # 向下滑动
    def swipeDown(self, time):
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, time)


    @try_to
    def wait_activity(self, activity_name, timeout=10):
        self.driver.wait_activity(activity_name, timeout, 1)

    @try_to
    def switch_to_alert(self):
        self.driver.switch_to.alert()

    @try_to
    def get_screenshot_as_file(self, path):
        self.driver.get_screenshot_as_file(path)
