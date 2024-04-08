# -*- coding: utf-8 -*-
"""
@Time ： 2024/3/15 10:59
@Auth ： 七月
@File ：makeLog.py
@IDE ：PyCharm
"""
import logging
import os

class Logger():
    # 配置日志记录器
    _instance = None

    def __new__(cls, level=logging.DEBUG):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logger = logging.getLogger()
            cls._instance.logger.setLevel(level)

            log_dir = os.path.abspath('./log')
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
            file_handler = logging.FileHandler(filename="./log/moco.log", encoding='utf-8', mode='a+')
            file_handler.setFormatter(formatter)
            cls._instance.logger.addHandler(file_handler)

        return cls._instance


    def debug(self,msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)


















