import configparser
import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
import zipfile

class TestEmail():
    def __init__(self,header,test_result):
        self.sender_name = ""
        self.sender_password = ""
        self.recevicer = ""
        self.smtp_server = "smtp.qq.com"  # qq邮箱的 SMTP 服务器地址
        self.smtp_port = 465  # qq 邮箱的 SMTP 端口（SSL）
        self.test_result =test_result
        self.header = header
        self.read_config()
    def read_config(self):
        try:
            current_folder_path = os.getcwd()
            config_file_path = os.path.join(current_folder_path, "config\\test_config.ini")
            config = configparser.ConfigParser()
            config.read(config_file_path)
            self.sender_name = config['email']['sender_name']
            self.sender_password = config['email']['sender_password']
            self.recevicer = config['email']['recevicer_name']
        except Exception as e:
            print(e)

    def create_zip_file(self):
        zip_filename = "test_results.zip"
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            # 假设测试结果文件为test_results.json
            with open("test_results.json", "w") as f:
                import json
                json.dump(self.test_results, f)
            zipf.write("test_results.json")
        return zip_filename

    def read_html_template(self):
        test_path = os.getcwd()
        email_folder = os.path.join(test_path, "utility", "email")
        env = Environment(loader=FileSystemLoader(email_folder))
        template = env.get_template('template.html')
        return template

    def add_test_result_to_template(self,template, result_dict):
        try:
            # common
            common =result_dict["common"]
            common["email_header"] = self.header
            result_list = []
            test_result_dict = result_dict["test_result"]
            number = 0
            for key, value in test_result_dict.items():
                number += 1
                value["number"] = number
                result_list.append(value)

            html_content = template.render(common =common, test_cases=result_list)
            return html_content

        except Exception as e:
            print(e)

    def send_email(self):
        msg = MIMEMultipart()
        msg["From"] = Header(self.sender_name)
        msg["To"] = Header(self.recevicer)
        msg["Subject"] = Header(self.header)
        template =  self.read_html_template()
        html_content = self.add_test_result_to_template(template, self.test_result)
        # 添加 HTML 邮件正文
        msg.attach(MIMEText(html_content, "html", "utf-8"))
        # # 添加附件
        # with open(zip_filename, "rb") as attachment:
        #     part = MIMEBase('application', 'octet-stream')
        #     part.set_payload(attachment.read())
        #     encoders.encode_base64(part)
        #     part.add_header(
        #         'Content-Disposition',
        #         f'attachment; filename={zip_filename}'
        #     )
        #     msg.attach(part)

        try:
            server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            server.login(self.sender_name, self.sender_password)  # 登录邮箱
            server.sendmail(self.sender_name, self.recevicer , msg.as_string())  # 发送邮件
            print("send email success")
        except Exception as e:
            print(f"send email fail: {e}")


if __name__ == '__main__':
    test_dict = {
        "common": {
            "test_type": "smoke_test",
            "test_file": "function_test",
            "total": 4,
            "pass": 1,
            "fail": 1,
            "crash": 0
        },
        "test_result": {
            "test_answers_to_chinese_question": {
                "case_name": "test_answers_to_chinese_question",
                "total": 2,
                "pass": 2,
                "fail": 0,
                "crash": 0,
                "fail_info": [
                ]
            },
            "test_answers_to_english_question": {
                "case_name": "test_answers_to_english_question",
                "total": 2,
                "pass": 1,
                "fail": 1,
                "crash": 0,
                "fail_info": [
                    "The answer is irrelevant to the question"
                ]
            }
        }
    }
    header = "smoke_test_function_test_1"
    send = TestEmail(header, test_dict)
    send.send_email()