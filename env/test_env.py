import glob
import importlib
import inspect
import os
import time
from datetime import datetime

from selenium.webdriver.chrome import webdriver

from utility.test_log.logger import TestLog
from utility.test_result.result import TestResult


def print_case_name(func):
    def wrapper(*args,**kwargs):
        print('[DEBUG]: enter {}()'.format(func.__name__))
        result = func(*args,**kwargs)
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

def read_config():
    pass

class TestEnv():
    def __init__(self,test_log_folder):
        self.test_result = TestResult()
        self.test_log = TestLog(self.get_test_log_path(test_log_folder))

    def get_test_log_path(self,test_log_folder):
        now = datetime.now()
        # 格式化时间为文件名格式
        str_now = now.strftime('%Y-%m-%d_%H-%M-%S')
        log_folder_name = "main" + str_now
        save_log_file = os.path.join(test_log_folder, log_folder_name)
        return save_log_file

    def find_and_execute_tests(self,directory, function_keyword):
        """
        在指定目录下查找包含特定函数关键字的 Python 文件，并执行其中以 test 开头的函数。

        :param directory: 要搜索的目录路径
        :param function_keyword: 要查找的函数关键字
        """
        # 遍历目录下的所有 .py 文件
        for file_path in glob.glob(os.path.join(directory, '*.py')):
            # 获取模块名（去掉 .py 后缀）
            module_name = os.path.splitext(os.path.basename(file_path))[0]

            # 动态加载模块
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # 检查模块中是否包含目标函数关键字
            has_keyword_flag = any(function_keyword in name for name in dir(module))
            if not has_keyword_flag:
                continue
            else:
                print(f'Found target keyword in file: {file_path}')

            # 遍历模块中的所有成员
            for name, obj in inspect.getmembers(module):
                # 检查是否是函数且以 test 开头
                if inspect.isfunction(obj) and name.startswith('test'):
                    print(f'Running test function: {name}')
                    try:
                        obj()  # 执行测试函数
                    except Exception as e:
                        print(f'Error running {name}: {e}')


