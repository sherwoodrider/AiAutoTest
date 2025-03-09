# 7. 多语言支持测试
# 目标：测试模型对多语言问题的支持能力。
#
# 示例用例：测试模型对非中文问题的回答能力。
import inspect
import time
from env.test_env import print_case_name
@print_case_name
def test_multilingual_support(test_env):
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
            "What is artificial intelligence?",  # 英文
            "¿Qué es la inteligencia artificial?",  # 西班牙语
            "인공지능이란 무엇인가요?"  # 韩语
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
            if test_env.check_keyword_relevance(question, answer):
                case_result["pass"] += 1
                test_env.test_log.log_info("The answer is relevant to the question")
            else:
                case_result["fail"] += 1
                fail_info = "The answer is irrelevant to the question"
                test_env.test_log.log_error(fail_info)
                case_result["fail_info"].append(fail_info)
        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)