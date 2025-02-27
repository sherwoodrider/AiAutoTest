import configparser
import os
import time
from datetime import datetime

from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from utility.test_log.logger import TestLog
from utility.test_result.result import TestResult


def print_case_name(func):
    def wrapper(test_env):
        test_env.test_log.log_info('enter {}()'.format(func.__name__))
        result = func(test_env)
        test_env.test_log.log_info('quit {}()'.format(func.__name__))
        return result
    return wrapper

def test_case(func):
    def wrapper(*args,**kwargs):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        time.sleep(3)
        driver.quit()
        print('[DEBUG]: enter {}()'.format(func.__name__))
        result = func(*args,**kwargs)
        return result
    return wrapper



class TestEnv():
    def __init__(self,test_log_folder):
        self.test_result = TestResult()
        self.test_log = TestLog(self.get_test_log_path(test_log_folder))
        self.login_name = ""
        self.login_password = ""
        self.sender_name = ""
        self.sender_password = ""
        self.recevicer_name = ""
        self.jenkins_name = ""
        self.jenkins_password = ""
        self.read_config()
        self.web_driver = None
        self.main_window_handle = None# 保存登录后的窗口句柄

    def read_config(self):
        try:
            current_folder_path = os.path.dirname(os.getcwd())
            config_file_path = os.path.join(current_folder_path, "config/test_config.ini")
            config = configparser.ConfigParser()
            config.read(config_file_path)

            self.login_name = config['deep_seek']['login_name']
            self.login_password = config['deep_seek']['password']

            self.sender_name = config['email']['sender_name']
            self.sender_password = config['email']['sender_password']
            self.recevicer_name = config['email']['recevicer_name']

            self.jenkins_name = config['jenkins']['name']
            self.jenkins_password = config['jenkins']['password']
        except Exception as e:
            print(e)
            self.test_log.log_critical(e)
    def login(self):
        try:
            # 初始化浏览器驱动（以 Chrome 为例）
            self.web_driver = webdriver.Chrome()  # 如果 ChromeDriver 不在 PATH 中，可以指定路径，如 webdriver.Chrome('/path/to/chromedriver')
            # 打开 DeepSeek 登录页面
            self.web_driver.get("https://www.deepseek.com/login")  # 替换为实际的登录页面 URL
            # 找到用户名和密码输入框（根据实际页面元素修改）
            username_input = self.web_driver.find_element(By.NAME, "username")  # 替换为实际的用户名输入框元素
            password_input = self.web_driver.find_element(By.NAME, "password")  # 替换为实际的密码输入框元素

            # 输入用户名和密码
            username_input.send_keys(self.login_name)
            password_input.send_keys(self.login_password)

            # 提交登录表单
            password_input.send_keys(Keys.RETURN)
            time.sleep(5)  # 等待登录完成
            self.main_window_handle = self.web_driver.current_window_handle  # 保存登录后的窗口句柄
        except Exception as e:
            print(e)
            self.test_log.log_critical(e)

    def quit(self):
        try:
            if not self.web_driver == None :
                self.web_driver.quit()
            else:
                error_info = "self.web_driver == None"
                self.test_log.log_error(error_info)
        except Exception as e:
            print(e)
            self.test_log.log_critical(e)

    def get_wed_driver_handle(self):
        try:
            if not self.main_window_handle == None :
                return self.main_window_handle
            else:
                error_info = "self.main_window_handle == None "
                self.test_log.log_error(error_info)
        except Exception as e:
            print(e)
            self.test_log.log_critical(e)

    def get_test_log_path(self,test_log_folder):
        now = datetime.now()
        # 格式化时间为文件名格式
        str_now = now.strftime('%Y-%m-%d_%H-%M-%S')
        log_folder_name = "main" + str_now
        save_log_file = os.path.join(test_log_folder, log_folder_name)
        return save_log_file




