import json
import os


class TestResult():
    def __init__(self,log_path):
        self.result_dict = {}
        self.log_path = log_path
        self.json_string = ""
        self.common_dict = {
            "test_type": "",
            "test_files": [],
            "total": 0,
            "pass": 0,
            "fail": 0,
            "crash": 0
        }
        self.final_result_dict = {}

    def result_to_json(self):
        # self.get_final_dict()
        json_string = json.dumps( self.final_result_dict, indent=4)  # indent 参数用于美化输出，缩进 4 个空格
        json_file_path = os.path.join(self.log_path, "test_result.json")
        # 将 JSON 字符串保存为文件
        with open(json_file_path, "w", encoding="utf-8") as file:
            file.write(json_string)
    def get_common_dict(self):
        try:
            for key, value in self.result_dict.items():
                self.common_dict["total"] += 1
                if value["crash"] > 0:
                    self.common_dict["crash"] += 1
                elif value["total"] > 0 and value["pass"] >0:
                    self.common_dict["pass"] += 1
                else:
                    self.common_dict["fail"] += 1
            self.final_result_dict["common"] = self.common_dict
            self.final_result_dict["test_result"] = self.result_dict
        except Exception as e :
            print(e)

    def get_final_dict(self):
        try:
            self.get_common_dict()
            self.final_result_dict["common"] = self.common_dict
            self.final_result_dict["test_result"] = self.result_dict
            return self.final_result_dict
        except Exception as e:
            print(e)
    def add_case_result(self,case_name,dict):
        self.result_dict[case_name] = dict