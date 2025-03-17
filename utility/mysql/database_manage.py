import configparser
import os
import mysql.connector
class DatabaseManager():
    def __init__(self,test_log_handle):
        self.test_log = test_log_handle
        self.conn = None
        self.read_config()
        self.host = ""
        self.port = ""
        self.user = ""
        self.password =""
        self.db_connection = self.connection()
        self.cursor = self.db_cursor()

    def read_config(self):
        try:
            current_folder_path = os.getcwd()
            config_file_path = os.path.join(current_folder_path, "config\\test_config.ini")
            config = configparser.ConfigParser()
            config.read(config_file_path)
            self.host = config.get("mysql", "host"),
            self.port = config.get("mysql", "port"),
            self.user = config.get("mysql", "user"),
            self.password = config.get("mysql", "password")
        except Exception as e:
            print(e)

    def connection(self):
        # 连接到 MySQL 服务器
        self.conn = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password
        )
        # 创建数据库
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS test_results_db")
        self.cursor.execute("USE test_results_db")
        # 创建表
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_results (
            id INT AUTO_INCREMENT PRIMARY KEY,
            test_case_name VARCHAR(255) NOT NULL,
            result VARCHAR(50) NOT NULL,
            crash INT,
            fail_info VARCHAR(255) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.conn.commit()
    def drop(self):
        self.cursor.execute("DROP DATABASE IF EXISTS test_results_db")
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
    def db_cursor(self):
        cursor = self.db_connection.cursor()
        return cursor

    def insert(self,case_name,test_result,crash,fail_info):
        try:
            # 将结果插入数据库
            sql = "INSERT INTO test_results (test_case_name, result,crash,fail_info) VALUES (%s, %s)"
            values = (case_name, test_result, crash, fail_info)
            self.db_cursor.execute(sql, values)
            self.db_connection.commit()
        except AssertionError as e:
            self.test_log.log_critical(e)

    def query(self, case_name):
        try:
            self.db_cursor.execute("SELECT result FROM test_results WHERE test_case_name = %s", (case_name,))
            row = self.db_cursor.fetchone()
            assert row is not None  # 查询到了结果
            assert row[1] == case_name
        except AssertionError as e:
            self.test_log.log_critical(e)
    def update(self, case_name,test_result,crash,fail_info):
        try:
            sql = "UPDATE test_results SET result = %s WHERE test_case_name = %s"
            values = (case_name, test_result, crash, fail_info)
            self.db_cursor.execute(sql, values)
            self.db_connection.commit()
            return self.db_cursor.rowcount  # 返回受影响的行数
        except AssertionError as e:
            self.test_log.log_critical(e)
    def delete(self, test_case_name):
        try:
            sql = "DELETE FROM test_results WHERE test_case_name = %s"
            self.db_cursor.execute(sql, (test_case_name,))
            self.db_connection.commit()
            return self.db_cursor.rowcount
        except AssertionError as e:
            self.test_log.log_critical(e)




