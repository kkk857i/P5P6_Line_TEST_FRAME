
# 1、日志的格式字符串如下：
#
# %(levelno)s:    #打印日志级别的数值
# %(levelname)s: #打印日志级别名称
# %(pathname)s: #打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s: #打印当前执行程序名
# %(funcName)s: #打印日志的当前函数
# %(lineno)d: #打印日志的当前行号
# %(asctime)s: #打印日志的时间
# %(thread)d: #打印线程ID
# %(threadName)s: #打印线程名称
# %(process)d: #打印进程ID
# %(message)s: #打印日志信息
# 要求把所有的格式都自己编写代码打印日志进行尝试

# 2、使用之前的excel接口测试用例模版，完成微信公众平台 删除标签、修改标签 （5条用例），并录入到接口测试框架中去执行
# 备注：根据分好的模块进行录入接口测试用例
#
# 3、完成日志模块的封装操作，在测试用例执行过程中进行日志输出实战操作


import logging

logger=logging.getLogger('work_01')
logger.setLevel(logging.DEBUG)

console_handler =logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s_k_%(levelno)s__%(levelname)s__%(pathname)s__"
                              # 时间     打印日志级别的数值       打印日志级别名称     日志路径
                              "%(filename)s__%(funcName)s__%(lineno)d__%(thread)d__"
                              #打印当前执行程序名  打印日志的当前函数  打印日志的当前行号  打印线程ID18208
                              "%(threadName)s__%(process)d__%(message)s")
                                #打印线程名称     打印进程ID    打印日志内容
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logger.info('hello word')















