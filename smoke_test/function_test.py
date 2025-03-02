import inspect
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from env.test_env import print_case_name



@print_case_name
def test_answers_to_chinese_question(test_env):
    try:
        case_result = {}
        questions = [
            "什么是人工智能",
            "如何设计一个数据库"
        ]
        for question in questions:
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\n answer: {answer}\n")
            case_result[question] = answer
        test_env.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)
@print_case_name
def test_answers_to_english_question(test_env):
    try:
        case_result = {}
        questions = [
            "What is artificial intelligence",
            "How to design a database"
        ]
        for question in questions:
            answer =  test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\n answer: {answer}\n")
            case_result[question] = answer
        test_env.add_case_result(str(inspect.currentframe().f_code.co_name),case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)