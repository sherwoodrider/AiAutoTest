import os

from selenium import webdriver
import time
import datetime

from env.test_env import TestEnv
from utility.email.send_email import TestEmail
from utility.test_log.logger import TestLog
from utility.test_result.result import TestResult
import glob
import importlib
import inspect

def find_and_execute_tests(test_env, directory, function_keyword):
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
        if not str(function_keyword) == (module_name):
            continue
        else:
            print(f'Found target keyword in file: {file_path}')

        # 遍历模块中的所有成员
        for name, obj in inspect.getmembers(module):
            # 检查是否是函数且以 test 开头
            if inspect.isfunction(obj) and name.startswith('test'):
                print(f'Running test function: {name}')
                try:
                    obj(test_env)  # 执行测试函数
                except Exception as e:
                    print(f'Error running {name}: {e}')

def get_save_log_path(test_path):
    now = datetime.datetime.now()
    # 格式化时间为文件名格式
    str_now = now.strftime('%Y_%m_%d_%H_%M_%S')
    log_folder_name = "aiautotest_" + str_now
    save_log_folder = os.path.join(test_path, "logs")
    test_log_folder = os.path.join(save_log_folder, log_folder_name)
    if not os.path.exists(test_log_folder):
        os.mkdir(test_log_folder)
    return test_log_folder


test_file_names = [
    "function_test",
    "ethical_test"
]
test_single_file_flag = True
test_file_name = "function_test"
test_type = "smoke_test"

if __name__ == '__main__':
    try:
        test_path = os.getcwd()
        test_log_folder = get_save_log_path(test_path)
        find_case_folder = os.path.join(test_path,test_type)
        test_env = TestEnv(test_log_folder)

        if test_single_file_flag:
            find_and_execute_tests(test_env,find_case_folder, test_file_name)
        else:
            for file_name in test_file_names:
                find_and_execute_tests(test_env,find_case_folder, file_name)

        test_env.test_result.result_to_json()
        email_header = test_type # default
        if test_single_file_flag:
            email_header += "(" + test_file_name + ")"
        else:
            count = 0
            for file_name in test_file_names:
                count += 1
                if count == 1:
                    email_header += "(" + file_name + ","
                elif count == len(test_file_names):
                    email_header += (file_name + ")")
                else:
                    email_header += (file_name + ",")

        test_result = test_env.test_result
        email_header = test_type
        email_send = TestEmail(email_header,test_env.test_result)
        email_send.send_email()
    except Exception as e:
        print(e)
