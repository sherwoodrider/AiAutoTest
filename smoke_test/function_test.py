import inspect
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from env.test_env import print_case_name

# 询问问题并获取答案
def ask_question(test_env,question):
    # 找到问题输入框（根据实际页面元素修改）
    question_input = test_env.driver.find_element(By.NAME, "question_input")  # 替换为实际的问题输入框元素
    question_input.send_keys(question)
    question_input.send_keys(Keys.RETURN)
    time.sleep(2)  # 等待答案生成
    # 获取答案（根据实际页面元素修改）
    answer = test_env.driver.find_element(By.CLASS_NAME, "answer").text  # 替换为实际的答案元素
    return answer

@print_case_name
def test_answers_to_chinese_question(test_env):
    try:
        case_result = {}
        questions = [
            "什么是人工智能？",
            # "Python 的主要特点是什么？",
            # "Selenium 是用来做什么的？",
            # "如何优化网页加载速度？",
            # "什么是机器学习？",
            # "如何学习编程？",
            # "什么是深度学习？",
            # "如何提高代码质量？",
            # "什么是 RESTful API？",
            "如何设计一个数据库？"
        ]
        for question in questions:
            answer = ask_question(test_env,question)
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
            answer = ask_question(test_env, question)
            test_env.test_log.log_info(f"question: {question}\n answer: {answer}\n")
            case_result[question] = answer
        test_env.add_case_result(str(inspect.currentframe().f_code.co_name),case_result)
        # test_env.test_result[str(inspect.currentframe().f_code.co_name)] = case_result
    except Exception as e:
        test_env.test_log.log_critical(e)