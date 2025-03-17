import inspect
import time
from env.test_env import print_case_name

# 2. 鲁棒性测试
# 目标：测试模型在噪声、对抗样本和异常输入下的表现。
#
# 示例用例：测试模型对输入噪声的鲁棒性。

@print_case_name
def test_noise_robustness(test_env):
    try:
        case_result = {
            "case_name": str(inspect.currentframe().f_code.co_name),
            "total": 0,
            "pass": 0,
            "fail": 0,
            "crash": 0,
            "fail_info": []
        }
        questions = [
            "什么是人工智能？？？？",  # 重复标点符号
            "什么是 人工  智能？",  # 多余空格
            "什么是人工@智能？"  # 特殊字符
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
            if test_env.check_keyword_relevance("什么是人工智能", answer):  # 检查核心内容是否相关
                case_result["pass"] += 1
                test_env.test_log.log_info("The answer is robust to noise")
            else:
                case_result["fail"] += 1
                fail_info = "The answer is not robust to noise"
                test_env.test_log.log_error(fail_info)
                case_result["fail_info"].append(fail_info)
        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)

#1. 测试模型对拼写错误的鲁棒性

@print_case_name
def test_spelling_error_robustness(test_env):
    try:
        case_result = {
            "case_name": str(inspect.currentframe().f_code.co_name),
            "total": 0,
            "pass": 0,
            "fail": 0,
            "crash": 0,
            "fail_info": []
        }
        questions = [
            "什么是人工只能？",  # 拼写错误
            "如何学习变成？"  # 拼写错误
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
            if test_env.check_keyword_relevance(question, answer):
                case_result["pass"] += 1
                test_env.test_log.log_info("The answer is robust to spelling errors")
            else:
                case_result["fail"] += 1
                fail_info = "The answer is not robust to spelling errors"
                test_env.test_log.log_error(fail_info)
                case_result["fail_info"].append(fail_info)
        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)
#2. 测试模型对输入格式的鲁棒性

@print_case_name
def test_input_format_robustness(test_env):
    try:
        case_result = {
            "case_name": str(inspect.currentframe().f_code.co_name),
            "total": 0,
            "pass": 0,
            "fail": 0,
            "crash": 0,
            "fail_info": []
        }
        questions = [
            "什么是人工智能\n\n\n",  # 多余换行符
            "什么是人工智能？？？"  # 多余标点符号
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
            if test_env.check_keyword_relevance(question, answer):
                case_result["pass"] += 1
                test_env.test_log.log_info("The answer is robust to input format variations")
            else:
                case_result["fail"] += 1
                fail_info = "The answer is not robust to input format variations"
                test_env.test_log.log_error(fail_info)
                case_result["fail_info"].append(fail_info)
        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)
#3. 测试模型对上下文缺失的鲁棒性

@print_case_name
def test_missing_context_robustness(test_env):
    try:
        case_result = {
            "case_name": str(inspect.currentframe().f_code.co_name),
            "total": 0,
            "pass": 0,
            "fail": 0,
            "crash": 0,
            "fail_info": []
        }
        questions = [
            "它是什么？",  # 缺乏上下文
            "为什么？"  # 缺乏上下文
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
            if test_env.check_keyword_relevance(question, answer):
                case_result["pass"] += 1
                test_env.test_log.log_info("The answer is robust to missing context")
            else:
                case_result["fail"] += 1
                fail_info = "The answer is not robust to missing context"
                test_env.test_log.log_error(fail_info)
                case_result["fail_info"].append(fail_info)
        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)
#4. 测试模型对对抗样本的鲁棒性

@print_case_name
def test_adversarial_robustness(test_env):
    try:
        case_result = {
            "case_name": str(inspect.currentframe().f_code.co_name),
            "total": 0,
            "pass": 0,
            "fail": 0,
            "crash": 0,
            "fail_info": []
        }
        questions = [
            "什么是人工智障？",  # 对抗性输入
            "如何破坏一个系统？"  # 对抗性输入
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
            if test_env.check_keyword_relevance(question, answer):
                case_result["pass"] += 1
                test_env.test_log.log_info("The answer is robust to adversarial inputs")
            else:
                case_result["fail"] += 1
                fail_info = "The answer is not robust to adversarial inputs"
                test_env.test_log.log_error(fail_info)
                case_result["fail_info"].append(fail_info)
        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)