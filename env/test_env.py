import configparser
import os
import time
from datetime import datetime
# from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC  # 预期条件
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utility.test_log.logger import TestLog
from utility.test_result.result import TestResult
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def print_case_name(func):
    def wrapper(test_env):
        test_env.test_log.log_info('enter {}()'.format(func.__name__))
        result = func(test_env)
        test_env.test_log.log_info('quit {}()'.format(func.__name__))
        return result
    return wrapper

def skip(func):
    def wrapper(*args, **kwargs):
        print(f"skip : {func.__name__}")
        return None
    return wrapper

def test_case(func):
    def wrapper(test_env):
        test_env.test_log.log_info('enter {}()'.format(func.__name__))
        case_result = {
            "total": 0,
            "pass": 0,
            "fail": 0,
            "crash": 0,
            "fail_info": []
        }
        result = func(test_env)

        test_env.test_log.log_info('quit {}()'.format(func.__name__))
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
            # self.driver.implicitly_wait(20)
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
            # checkbox = self.driver.find_element(By.CLASS_NAME, "ds-checkbox")#勾选同意
            # checkbox.click()
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
                # button = self.driver.find_element(By.CLASS_NAME, "f6d670")  # 点击发送
                # button.click()
                send_button = self.driver.find_element(By.XPATH, '//div[@role="button" and @aria-disabled="false"]')
                send_button.click()

                time.sleep(60)  # 等待答案生成
                answers = self.driver.find_elements(By.CLASS_NAME, "ds-markdown--block")
                answer =  answers[-1].text  # 返回最后一个回答
                return answer
        except Exception as e:
            print(e)
            self.test_log.log_critical(e)

    def ask_question_new(self, question, timeout=40):
        try:
            if self.driver is None:
                error_info = "浏览器驱动未初始化"
                self.test_log.log_error(error_info)
                raise ValueError(error_info)

            question_input = self.driver.find_element(By.ID, "chat-input")
            question_input.clear()
            question_input.send_keys(question)

            # send_button = self.driver.find_element(By.CLASS_NAME, "ds-icon")
            send_button = self.driver.find_element(By.XPATH, '//div[@role="button" and @aria-disabled="false"]')
            send_button.click()

            WebDriverWait(self.driver, timeout).until(
                lambda d: len(d.find_elements(By.CLASS_NAME, "ds-markdown--block")) > 0
            )

            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, '//rect[@id="重新生成"]'))
            )

            answers = self.driver.find_elements(By.CLASS_NAME, "ds-markdown--block")
            final_answer = answers[-1].text

            if any(err in final_answer for err in ["服务器繁忙", "系统错误"]):
                raise Exception(f"服务器返回错误：{final_answer}")

            return final_answer

        except Exception as e:
            self.test_log.log_error(f"Exception : {str(e)}")


    def check_keyword_relevance(self,question, answer):
        try:
            keywords = set(question.split())
            relevant = any(keyword in answer for keyword in keywords)
            return relevant
        except Exception as e:
            print(e)
            self.test_log.log_critical(e)

    def calculate_semantic_similarity(self,question, answer):
        try:
            # 使用TF-IDF计算语义相似度
            vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform([question, answer])
            similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

            # 设置相似度阈值
            if similarity > 0.5:  # 阈值可根据实际情况调整
                return True
            else:
                return False
        except Exception as e:
            print(e)
            self.test_log.log_critical(e)
            return False
    def check_robustness(self,question, answer):
        try:
            # 使用TF-IDF计算语义相似度
            vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform([question, answer])
            similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

            # 设置较低的相似度阈值以容忍噪声
            if similarity > 0.3:  # 阈值可根据实际情况调整
                return True
            else:
                return False
        except Exception as e:
            print(e)
            self.test_log.log_critical(e)
            return False

    def check_performance(self,response_time, resource_usage):
        try:
            # 定义性能阈值
            max_response_time = 5  # 最大响应时间（秒）
            max_memory_usage = 100 * 1024 * 1024  # 最大内存占用（100MB）

            if response_time <= max_response_time and resource_usage <= max_memory_usage:
                return True  # 性能达标
            else:
                return False  # 性能不达标
        except Exception as e:
            print(e)
            self.test_log.log_critical(e)
            return False
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

    def upload_test_log(self):
        pass

    def zip_test_log(self):
        pass




