# 6. 可解释性测试
# 目标：评估模型的决策过程是否可解释，是否能够提供合理的解释。
#
# 示例用例：测试模型是否能够解释其回答的逻辑。
import inspect
import time
from env.test_env import print_case_name

@print_case_name
def test_answer_explainability(test_env):
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
            "为什么天空是蓝色的？",
            "请解释一下量子力学的基本原理"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
            if test_env.check_explainability(answer):  # 检查回答是否包含解释性内容
                case_result["pass"] += 1
                test_env.test_log.log_info("The answer is explainable")
            else:
                case_result["fail"] += 1
                fail_info = "The answer lacks explainability"
                test_env.test_log.log_error(fail_info)
                case_result["fail_info"].append(fail_info)
        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)

#1. 测试模型是否解释其决策逻辑

@print_case_name
def test_decision_explainability(test_env):
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
            "为什么你认为地球是圆的？",
            "请解释一下你的回答逻辑"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
            if test_env.check_explainability(answer):
                case_result["pass"] += 1
                test_env.test_log.log_info("The answer is explainable")
            else:
                case_result["fail"] += 1
                fail_info = "The answer lacks explainability"
                test_env.test_log.log_error(fail_info)
                case_result["fail_info"].append(fail_info)
        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)
#2. 测试模型是否提供来源引用

@print_case_name
def test_source_citation(test_env):
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
            "请提供关于量子力学的来源",
            "你的回答基于哪些研究？"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
            if test_env.check_source_citation(answer):
                case_result["pass"] += 1
                test_env.test_log.log_info("The answer provides source citation")
            else:
                case_result["fail"] += 1
                fail_info = "The answer lacks source citation"
                test_env.test_log.log_error(fail_info)
                case_result["fail_info"].append(fail_info)
        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)
#3. 测试模型是否解释复杂概念

@print_case_name
def test_complex_concept_explainability(test_env):
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
            "请解释一下量子纠缠",
            "什么是区块链技术？"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
            if test_env.check_explainability(answer):
                case_result["pass"] += 1
                test_env.test_log.log_info("The answer explains complex concepts")
            else:
                case_result["fail"] += 1
                fail_info = "The answer fails to explain complex concepts"
                test_env.test_log.log_error(fail_info)
                case_result["fail_info"].append(fail_info)
        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)
#4. 测试模型是否解释其局限性

@print_case_name
def test_limitation_explainability(test_env):
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
            "你的回答有什么局限性？",
            "你在哪些情况下可能出错？"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
            if test_env.check_explainability(answer):
                case_result["pass"] += 1
                test_env.test_log.log_info("The answer explains its limitations")
            else:
                case_result["fail"] += 1
                fail_info = "The answer fails to explain its limitations"
                test_env.test_log.log_error(fail_info)
                case_result["fail_info"].append(fail_info)
        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)