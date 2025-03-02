import configparser
import os
import time
from datetime import datetime

from selenium.webdriver import Keys
from selenium import webdriver
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
        self.test_log_folder = test_log_folder
        self.test_result = TestResult(self.test_log_folder)
        self.test_log = TestLog(self.get_test_log_path(test_log_folder))
        self.login_name = ""
        self.login_password = ""
        # self.sender_name = ""
        # self.sender_password = ""
        # self.recevicer_name = ""
        self.jenkins_name = ""
        self.jenkins_password = ""
        self.read_config()
        self.driver = None
        self.main_window_handle = None# 保存登录后的窗口句柄
        self.login()
    def __del__(self):
        self.quit()

    def read_config(self):
        try:
            # 获取 D:\code_repo\AiAutoTest\logs
            logs_dir = os.path.dirname(self.test_log_folder)
            # 获取 D:\code_repo\AiAutoTest
            base_dir = os.path.dirname(logs_dir)
            config_file_path = os.path.join(base_dir, "config/test_config.ini")
            config = configparser.ConfigParser()
            config.read(config_file_path)

            self.login_name = config['deep_seek']['login_name']
            self.login_password = config['deep_seek']['password']

            # self.sender_name = config['email']['sender_name']
            # self.sender_password = config['email']['sender_password']
            # self.recevicer_name = config['email']['recevicer_name']

            self.jenkins_name = config['jenkins']['name']
            self.jenkins_password = config['jenkins']['password']
        except Exception as e:
            print(e)
            self.test_log.log_critical(e)
    def login(self):
        try:
            self.driver = webdriver.Chrome()
            # 打开 DeepSeek 登录页面
            self.driver.get("https://chat.deepseek.com/sign_in")
            element = self.driver.find_element(By.XPATH, "//div[text()='密码登录']")
            element.click()
            time.sleep(2)
            # # 找到用户名和密码输入框（根据实际页面元素修改）
            username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='请输入手机号/邮箱地址']")
            password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']")
            username_input.send_keys(self.login_name)
            password_input.send_keys(self.login_password)
            checkbox = self.driver.find_element(By.CLASS_NAME, "ds-checkbox")#勾选同意
            checkbox.click()
            login_input = self.driver.find_element(By.XPATH, "//div[text()='登录']")  # 点击登录
            login_input.click()
            time.sleep(5)  # 等待登录完成
        except Exception as e:
            print(e)
            self.test_log.log_critical(e)

    def quit(self):
        try:
            if not self.driver == None :
                self.driver.quit()
            else:
                error_info = "self.driver == None"
                self.test_log.log_error(error_info)
        except Exception as e:
            print(e)
            self.test_log.log_critical(e)

    def ask_question(self,question):
        try:
            if self.driver == None:
                error_info = "self.driver == None"
                self.test_log.log_error(error_info)
            else:
                question_input = self.driver.find_element(By.ID, "chat-input")
                question_input.send_keys(question)
                time.sleep(2)
                button = self.driver.find_element(By.CLASS_NAME, "f6d670")  # 点击发送
                button.click()
                time.sleep(60)  # 等待答案生成
                answer = self.driver.find_element(By.CLASS_NAME, "ds-markdown--block").text  # 获取纯文本内容
                return answer
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
        str_now = now.strftime('%Y_%m_%d_%H_%M_%S')
        log_folder_name = "main_" + str_now + ".log"
        save_log_file = os.path.join(test_log_folder, log_folder_name)
        return save_log_file

    def save_json(self):
        pass

    def upload_test_log(self):
        pass

    def zip_test_log(self):
        pass




