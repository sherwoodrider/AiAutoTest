import json
import os


class TestResult():
    def __init__(self):
        self.result_dict = {}
        self.json_string = ""

    def result_to_json(self):
        json_string = json.dumps(self.result_dict, indent=4)  # indent 参数用于美化输出，缩进 4 个空格
        test_path = os.getcwd()
        save_log_folder = os.path.join(test_path, "logs")
        json_file_path = os.path.join(save_log_folder, "test_result.json")
        # 将 JSON 字符串保存为文件
        with open(json_file_path, "w", encoding="utf-8") as file:
            file.write(json_string)
    def add_case_result(self,case_name,dict):
        self.result_dict[case_name] = dict