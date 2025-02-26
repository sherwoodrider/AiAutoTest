import logging
import time
import os
import datetime


class TestLog():
    def __init__(self,log_file='main.log', level=logging.DEBUG):
        """
                    初始化 Logger
                    :param name: Logger 的名称
                    :param log_file: 日志文件名
                    :param level: 日志级别
            """
        # 配置 logging
        logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=log_file,
        filemode='a'  # 追加模式
        )
        self.log_handle = ""
        # 创建一个 logger 实例
        self.logger = logging.getLogger(log_file)

    def log_debug(self, message):
        """记录 DEBUG 级别的日志"""
        self.logger.debug(message)

    def log_info(self, message):
        """记录 INFO 级别的日志"""
        self.logger.info(message)

    def log_warning(self, message):
        """记录 WARNING 级别的日志"""
        self.logger.warning(message)

    def log_error(self, message, exc_info=False):
        """记录 ERROR 级别的日志，可选是否记录异常信息"""
        self.logger.error(message, exc_info=exc_info)

    def log_critical(self, message):
        """记录 CRITICAL 级别的日志"""
        self.logger.critical(message)




