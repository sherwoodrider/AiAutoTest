import json

class TestResult():
    def __init__(self):
        self.result_dict = {}

    def result_to_json(self):
        json_file  = json.dump(self.result_dict)
        pass
    def add_case_result(self,case_name,dict):
        pass