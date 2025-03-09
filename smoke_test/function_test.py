import inspect
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from env.test_env import print_case_name
#1. 测试AI对简单中文问题的回答
@print_case_name
def test_simple_chinese_question(test_env):

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
            "什么是机器学习",
            "Python是什么",
            "如何学习编程"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
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
#2. 测试AI对复杂问题的回答
@print_case_name
def test_complex_question(test_env):
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
            "如何设计一个高可用的分布式系统",
            "深度学习和机器学习有什么区别"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
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
#3. 测试AI对多轮对话的支持
@print_case_name
def test_multi_turn_conversation(test_env):
    try:
        case_result = {
            "case_name": str(inspect.currentframe().f_code.co_name),
            "total": 0,
            "pass": 0,
            "fail": 0,
            "crash": 0,
            "fail_info": []
        }
        conversations = [
            ("什么是人工智能", "人工智能有哪些应用"),
            ("Python是什么", "Python适合做什么类型的项目")
        ]
        for question1, question2 in conversations:
            case_result["total"] += 1
            answer1 = test_env.ask_question(question1)
            answer2 = test_env.ask_question(question2, context=answer1)
            test_env.test_log.log_info(f"Q1: {question1}\nA1: {answer1}\nQ2: {question2}\nA2: {answer2}\n")
            if test_env.check_keyword_relevance(question2, answer2):
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
#4. 测试AI对长文本问题的回答
@print_case_name
def test_long_text_question(test_env):
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
            "请详细解释一下Transformer模型的结构和工作原理，包括Self-Attention机制的具体实现细节。"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
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
#5. 测试AI对边界问题的回答
@print_case_name
def test_edge_case_questions(test_env):
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
            "",  # 空问题
            " ",  # 空格问题
            "1234567890",  # 纯数字问题
            "!@#$%^&*()"  # 特殊字符问题
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
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
#6. 测试AI对技术术语的理解
@print_case_name
def test_technical_term_understanding(test_env):
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
            "什么是梯度下降？",
            "解释一下反向传播算法",
            "什么是卷积神经网络？"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
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
#7. 测试AI对数学问题的回答
@print_case_name
def test_math_question(test_env):
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
            "2 + 2等于多少？",
            "求解方程x^2 - 4 = 0",
            "什么是微积分？"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
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
#8. 测试AI对历史问题的回答
@print_case_name
def test_history_question(test_env):
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
            "第二次世界大战是什么时候发生的？",
            "谁发明了电灯？",
            "中国的四大发明是什么？"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
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

#9. 测试AI对多语言问题的回答
@print_case_name
def test_multilingual_question(test_env):
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
            "What is artificial intelligence?",  # 英文问题
            "¿Qué es la inteligencia artificial?",  # 西班牙语问题
            "인공지능이란 무엇인가요?"  # 韩语问题
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
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

#10. 测试AI对模糊问题的回答
@print_case_name
def test_ambiguous_question(test_env):
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
            "这是什么？",  # 模糊问题
            "为什么？",  # 模糊问题
            "怎么办？"  # 模糊问题
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
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

#11. 测试AI对编程问题的回答
@print_case_name
def test_programming_question(test_env):
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
            "如何在Python中实现一个快速排序算法？",
            "JavaScript中的闭包是什么？",
            "如何用C++实现一个单例模式？"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
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

#12. 测试AI对科学问题的回答
@print_case_name
def test_science_question(test_env):
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
            "什么是量子力学？",
            "DNA的结构是什么？",
            "黑洞是如何形成的？"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
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

#13. 测试AI对文化问题的回答

@print_case_name
def test_culture_question(test_env):
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
            "中国的春节有哪些传统习俗？",
            "日本的茶道文化是什么？",
            "印度的排灯节是什么？"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
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

# 14. 测试AI对健康问题的回答
@print_case_name
def test_health_question(test_env):
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
            "如何预防感冒？",
            "高血压患者应该注意什么？",
            "什么是健康的生活方式？"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
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

#15. 测试AI对经济问题的回答
@print_case_name
def test_economics_question(test_env):
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
            "什么是通货膨胀？",
            "如何理解供需关系？",
            "全球化的影响是什么？"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
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

