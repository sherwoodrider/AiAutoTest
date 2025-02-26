import os

from selenium import webdriver
import time
import datetime

from env.test_env import TestEnv
from utility.test_log.logger import TestLog
from utility.test_result.result import TestResult




def get_save_log_path(test_path):
    now = datetime.now()
    # 格式化时间为文件名格式
    str_now = now.strftime('%Y-%m-%d_%H-%M-%S')
    log_folder_name = "aiautotest" + str_now
    save_log_folder = os.path.join(test_path, "logs")
    test_log_folder = os.path.join(save_log_folder, log_folder_name)
    if not os.path.exists(test_log_folder):
        os.mkdir(test_log_folder)


test_file_names = [
    "function_test",
    "ethical_test"
]
test_single_file_flag = False
test_file_name = "function_test"
test_type = "smoke_test"

if __name__ == '__main__':
    try:
        test_path = os.getcwd()
        test_log_folder = get_save_log_path(test_path)
        find_case_folder = os.path.join(test_path,test_type)
        test_env = TestEnv(test_log_folder)
        if test_single_file_flag:
            test_env.find_and_execute_tests(find_case_folder, test_file_name)
        else:
            for file_name in test_file_names:
                test_env.find_and_execute_tests(find_case_folder, file_name)
    except Exception as e:
        print(e)
