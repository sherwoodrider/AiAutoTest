import configparser
import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class TestEmail():
    def __init__(self,header,test_result):
        self.sender_name = ""
        self.sender_password = ""
        self.recevicer = ""
        self.smtp_server = "smtp.163.com"  # 163 邮箱的 SMTP 服务器地址
        self.smtp_port = 465  # 163 邮箱的 SMTP 端口（SSL）
        self.email_address = "your_email@163.com"
        self.email_password = "your_authorization_code"  # 授权码
        self.test_result =test_result
        self.header = header
        self.read_config()
    def read_config(self):
        try:
            current_folder_path = os.path.dirname(os.getcwd())
            config_file_path = os.path.join(current_folder_path, "config/test_config.ini")
            config = configparser.ConfigParser()
            config.read(config_file_path)
            self.sender_name = config['email']['sender_name']
            self.sender_password = config['email']['sender_password']
            self.recevicer = config['email']['recevicer_name']
        except Exception as e:
            print(e)
    def read_html_template(self):
        test_path = os.getcwd()
        email_folder = os.path.join(test_path, "utility/email")
        template_path = os.path.join(email_folder, "template.html")
        with open(template_path, "r", encoding="utf-8") as file:
            return file.read()

    def add_test_result_to_template(self,template, result_dict):
        for key, value in result_dict.items():
            template = template.replace("{{" + key + "}}", value)
        return template
    def send_email(self):
        msg = MIMEMultipart()
        msg["From"] = Header(self.email_address)
        msg["To"] = Header(self.recevicer)
        msg["Subject"] = Header(self.header)
        template =  self.read_html_template()
        html_content = self.add_test_result_to_template(template, self.test_result)
        # 添加 HTML 邮件正文
        msg.attach(MIMEText(html_content, "html", "utf-8"))

        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.email_address, self.email_password)  # 登录邮箱
                server.sendmail(self.email_address, self.recevicer , msg.as_string())  # 发送邮件
                print("send email success")
        except Exception as e:
            print(f"send email success fail: {e}")