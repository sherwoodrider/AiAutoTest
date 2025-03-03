import inspect
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from env.test_env import print_case_name

@print_case_name
def test_answers_to_chinese_question(test_env):
    try:
        case_result = {
            "case_name":str(inspect.currentframe().f_code.co_name),
            "total":0,
            "pass":0,
            "fail":0,
            "crash":0,
            "fail_info":[]
            }
        questions = [
            "什么是人工智能",
            # "如何设计一个数据库"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\n answer: {answer}\n")
            if test_env.check_keyword_relevance(question, answer):
                case_result["pass"] += 1
                test_env.test_log.log_info("The answer is related to the question")
            else:
                case_result["fail"] += 1
                fail_info = "The answer is irrelevant to the question"
                test_env.test_log.log_error(fail_info)
                case_result["fail_info"].append(fail_info)
        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)
@print_case_name
def test_answers_to_english_question(test_env):
    try:
        case_result = {
            # "test_type": str(inspect.getfile(inspect.currentframe())),
            "case_name": str(inspect.currentframe().f_code.co_name),
            "total": 0,
            "pass": 0,
            "fail": 0,
            "crash": 0,
            "fail_info": []
        }
        questions = [
            # "What is artificial intelligence",
            "How to design a database"
        ]
        for question in questions:
            case_result["total"] += 1
            answer =  test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\n answer: {answer}\n")
            if test_env.check_keyword_relevance(question, answer):
                case_result["pass"] += 1
                test_env.test_log.log_info("The answer is related to the question")
            else:
                case_result["fail"] += 1
                fail_info = "The answer is irrelevant to the question"
                test_env.test_log.log_error(fail_info)
                case_result["fail_info"].append(fail_info)
        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name),case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)