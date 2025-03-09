
import inspect
import time
from env.test_env import print_case_name

# 4. 用户体验测试
# 目标：评估模型与用户的交互体验。
# 示例用例：测试模型对用户意图的理解能力。

@print_case_name
def test_user_intent_understanding(test_env):
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
            "你能帮我写一封感谢信吗？",
            "我想知道今天的天气"
        ]
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
            if test_env.check_keyword_relevance(question, answer):
                case_result["pass"] += 1
                test_env.test_log.log_info("The answer correctly understands user intent")
            else:
                case_result["fail"] += 1
                fail_info = "The answer does not understand user intent"
                test_env.test_log.log_error(fail_info)
                case_result["fail_info"].append(fail_info)
        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)