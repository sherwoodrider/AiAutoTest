import inspect
import time
from env.test_env import print_case_name

# 1. 性能测试
# 目标：评估模型的响应速度、资源占用和扩展性。
#
# 示例用例：测试模型在高并发请求下的响应时间。
@print_case_name
def test_high_concurrency_performance(test_env):
    try:
        case_result = {
            "case_name": str(inspect.currentframe().f_code.co_name),
            "total": 0,
            "pass": 0,
            "fail": 0,
            "crash": 0,
            "fail_info": []
        }
        questions = ["什么是人工智能？"] * 100  # 模拟100个并发请求
        start_time = time.time()

        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")

        end_time = time.time()
        response_time = end_time - start_time
        test_env.test_log.log_info(f"Total response time for 100 requests: {response_time} seconds")

        if response_time < 10:  # 假设10秒是可接受的上限
            case_result["pass"] += 1
            test_env.test_log.log_info("Performance test passed: Response time is acceptable")
        else:
            case_result["fail"] += 1
            fail_info = f"Performance test failed: Response time {response_time} seconds is too slow"
            test_env.test_log.log_error(fail_info)
            case_result["fail_info"].append(fail_info)

        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)

# 1. 测试模型在低资源环境下的表现
@print_case_name
def test_low_resource_performance(test_env):
    try:
        case_result = {
            "case_name": str(inspect.currentframe().f_code.co_name),
            "total": 0,
            "pass": 0,
            "fail": 0,
            "crash": 0,
            "fail_info": []
        }
        questions = ["什么是人工智能？"] * 10  # 模拟10个请求
        start_time = time.time()

        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")

        end_time = time.time()
        response_time = end_time - start_time
        test_env.test_log.log_info(f"Total response time for 10 requests: {response_time} seconds")

        if response_time < 5:  # 假设5秒是可接受的上限
            case_result["pass"] += 1
            test_env.test_log.log_info("Performance test passed: Response time is acceptable in low resource environment")
        else:
            case_result["fail"] += 1
            fail_info = f"Performance test failed: Response time {response_time} seconds is too slow in low resource environment"
            test_env.test_log.log_error(fail_info)
            case_result["fail_info"].append(fail_info)

        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)

# 2. 测试模型的内存占用

@print_case_name
def test_memory_usage(test_env):
    try:
        case_result = {
            "case_name": str(inspect.currentframe().f_code.co_name),
            "total": 0,
            "pass": 0,
            "fail": 0,
            "crash": 0,
            "fail_info": []
        }
        import psutil
        process = psutil.Process()
        initial_memory = process.memory_info().rss  # 获取初始内存占用

        questions = ["什么是人工智能？"] * 100  # 模拟100个请求
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")

        final_memory = process.memory_info().rss  # 获取最终内存占用
        memory_usage = final_memory - initial_memory
        test_env.test_log.log_info(f"Memory usage for 100 requests: {memory_usage} bytes")

        if memory_usage < 100 * 1024 * 1024:  # 假设100MB是可接受的上限
            case_result["pass"] += 1
            test_env.test_log.log_info("Memory usage is within acceptable limits")
        else:
            case_result["fail"] += 1
            fail_info = f"Memory usage {memory_usage} bytes exceeds acceptable limits"
            test_env.test_log.log_error(fail_info)
            case_result["fail_info"].append(fail_info)

        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)

# 3. 测试模型的CPU占用
@print_case_name
def test_cpu_usage(test_env):
    try:
        case_result = {
            "case_name": str(inspect.currentframe().f_code.co_name),
            "total": 0,
            "pass": 0,
            "fail": 0,
            "crash": 0,
            "fail_info": []
        }
        import psutil
        process = psutil.Process()
        initial_cpu = process.cpu_percent(interval=1)  # 获取初始CPU占用

        questions = ["什么是人工智能？"] * 100  # 模拟100个请求
        for question in questions:
            case_result["total"] += 1
            answer = test_env.ask_question(question)
            test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")

        final_cpu = process.cpu_percent(interval=1)  # 获取最终CPU占用
        cpu_usage = final_cpu - initial_cpu
        test_env.test_log.log_info(f"CPU usage for 100 requests: {cpu_usage}%")

        if cpu_usage < 50:  # 假设50%是可接受的上限
            case_result["pass"] += 1
            test_env.test_log.log_info("CPU usage is within acceptable limits")
        else:
            case_result["fail"] += 1
            fail_info = f"CPU usage {cpu_usage}% exceeds acceptable limits"
            test_env.test_log.log_error(fail_info)
            case_result["fail_info"].append(fail_info)

        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)

# 4. **测试模型在高负载下的稳定性
@print_case_name
def test_high_load_stability(test_env):
    try:
        case_result = {
            "case_name": str(inspect.currentframe().f_code.co_name),
            "total": 0,
            "pass": 0,
            "fail": 0,
            "crash": 0,
            "fail_info": []
        }
        questions = ["什么是人工智能？"] * 1000  # 模拟1000个请求
        crash_count = 0

        for question in questions:
            case_result["total"] += 1
            try:
                answer = test_env.ask_question(question)
                test_env.test_log.log_info(f"question: {question}\nanswer: {answer}\n")
            except Exception as e:
                crash_count += 1
                test_env.test_log.log_critical(f"Crash occurred: {e}")

        if crash_count == 0:
            case_result["pass"] += 1
            test_env.test_log.log_info("Model is stable under high load")
        else:
            case_result["fail"] += 1
            fail_info = f"Model crashed {crash_count} times under high load"
            test_env.test_log.log_error(fail_info)
            case_result["fail_info"].append(fail_info)

        test_env.test_result.add_case_result(str(inspect.currentframe().f_code.co_name), case_result)
    except Exception as e:
        test_env.test_log.log_critical(e)
