import importlib
import inspect
import json
import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from env.test_env import TestEnv
from utility.ui.main_window import Ui_MainWindow
from utility.ui.open_file import Ui_dialog
import datetime
def get_save_log_path(test_path):
    now = datetime.datetime.now()
    # 格式化时间为文件名格式
    str_now = now.strftime('%Y_%m_%d_%H_%M_%S')
    log_folder_name = "aiautotest_" + str_now
    save_log_folder = os.path.join(test_path, "logs")
    test_log_folder = os.path.join(save_log_folder, log_folder_name)
    if not os.path.exists(test_log_folder):
        os.mkdir(test_log_folder)
    return test_log_folder
def find_case_and_run(test_env,test_type,test_cases,output_test_edit):
    try:
        module_name = test_type
        if not module_name:
            raise ValueError(f"未知的测试类型: {test_type}")

        module = importlib.import_module(module_name)

        test_functions = [
            (name, func) for name, func in inspect.getmembers(module)
            if name.startswith('test_') and inspect.isfunction(func)
        ]

        executed_count = 0
        for case_name in test_cases:
            for name, func in test_functions:
                if name == case_name:
                    try:
                        result = func(test_env)
                        output_test_edit.append(
                            f"[{case_name}] 执行成功\n"
                            f"结果: {result}\n"
                            f"{'-' * 50}\n"
                        )
                        executed_count += 1
                    except Exception as e:
                        output_test_edit.append(
                            f"[{case_name}] 执行失败\n"
                            f"错误: {str(e)}\n"
                            f"{'-' * 50}\n"
                        )
                    break
            else:
                output_test_edit.append(
                    f"[{case_name}] 未找到该测试用例\n"
                    f"{'-' * 50}\n"
                )

        output_test_edit.append(
            f"\n执行完成\n"
            f"总指定用例数: {len(test_cases)}\n"
            f"成功执行数: {executed_count}\n"
        )

    except Exception as e:
        print(e)

class QtMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.test_cases = []
        self.test_type = ""
        self.test_plan_json_path = ""
        super().__init__()
        self.setupUi(self)
        self.open_file_btn.clicked.connect(self.select_json_file)
        self.run_test_btn.clicked.connect(self.run_test)
        self.json_data = None

    def select_json_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择 JSON 文件", "", "JSON 文件 (*.json);;所有文件 (*)"
        )
        if file_path:
            self.json_file_path_textEdit.setText(f"{file_path}")
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.json_data = json.load(f)
                    self.display_json_content()
                    self.run_test_btn.setEnabled(True)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"无法读取 JSON 文件: {str(e)}")
                self.json_data = None
                self.run_test_btn.setEnabled(False)

    def display_json_content(self):
        if not self.json_data:
            return
        self.test_type = self.json_data.get("test_type", "未指定测试类型")
        self.test_type_TextEdit.setPlainText(f"{self.test_type}")

    def run_test(self):
        if len(self.test_cases) == 0 :
            QMessageBox.critical(self, "错误", f"test_cases 列表为空")
        else:
            self.output_test_edit.append("********test begin********")
            self.output_test_edit.clear()
            self.output_test_edit.append(f"开始执行 {self.test_type} 测试...\n")
            test_path = os.getcwd()
            test_log_folder = get_save_log_path(test_path)
            test_env = TestEnv(test_log_folder)
            find_case_and_run(test_env,self.test_type,self.test_cases,self.output_test_edit)


class QtOpenFile(QtWidgets.QDialog, Ui_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


