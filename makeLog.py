# -*- coding: utf-8 -*-
"""
@Time ： 2024/3/15 10:59
@Auth ： 七月
@File ：makeLog.py
@IDE ：PyCharm
"""
import logging
import os

class logger():
    # 配置日志记录器
    def __init__(self,level=logging.DEBUG):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)
        #获取当前脚本的绝对路径
        log_dir = os.path.abspath('./log')
        if not os.path.exists(log_dir):
            try:
                os.mkdir(log_dir)
                if os.path.exists('./log/moco.log'):
                    pass
                else:
                    try:
                        with open('./log/moco.log', 'a+',encoding='utf-8') as file:
                            pass
                    except IOError as e:
                        pass
            except OSError as e:
                pass
        else:
            pass
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s",datefmt='%Y-%m-%d %H:%M:%S')

        file_handler = logging.FileHandler(filename="./log/moco.log", encoding='utf-8', mode='a+')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)


    def debug(self,msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)


















