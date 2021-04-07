

import os
import logging
import time

#api_test_log_20210317.log

current_path = os.path.dirname(__file__)
log_output_path = os.path.join(current_path,'..','logs')

class LogUtils:
    def __init__(self, log_path=log_output_path):
        self.log_file_path = os.path.join(log_path,'api_test_log_%s.log' % time.strftime('%Y%m%d'))
        self.__logger = logging.getLogger("WX_api_test_log")
        self.__logger.setLevel(logging.DEBUG)     #10  默认30


        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self.log_file_path,'a',encoding='utf-8')
        formatter = logging.Formatter("%(asctime)s_k_%(name)s__%(levelname)s__%(message)s")
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.__logger.addHandler(console_handler)
        self.__logger.addHandler(file_handler)

        console_handler.close() #防止日志打印重复
        file_handler.close()

    def get_logger(self):
        return self.__logger

#建议日志用一个对象去输出
logger=LogUtils().get_logger()

if __name__=='__main__':
    logger.info('执行接口测试用例开始')
    logger.info('测试用例开始')
    # logger=LogUtils().get_logger()
    # logger.info('执行接口测试用例开始..')
    # LogUtils().logger.info('接口测试用例开始')







