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

    for file_path in glob.glob(os.path.join(directory, '*.py')):
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if not str(function_keyword) == (module_name):
            continue
        else:
            print(f'Found target keyword in file: {file_path}')
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) and name.startswith('test'):
                print(f'Running test function: {name}')
                try:
                    obj(test_env)
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
    "ethical_test",
    "robustness_test"
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

        test_result = test_env.test_result.get_final_dict()
        test_env.test_result.result_to_json()
        email_send = TestEmail(email_header,test_result)
        email_send.send_email()
    except Exception as e:
        print(e)
