
import logging

#相当于输出语句，默认输出error语句，info是不能输出的
# logging.info('info！！')
# logging.error('Error')


log_obj=logging.getLogger('p5p6')   #日志的名称

log_obj.setLevel(10)    #设置日志的默认级别  一般配置最小的级别
handler1=logging.StreamHandler()    #创建handler对象：handler对象给日志进行级别、格式等配置用的，日志的输出方式
handler1.setLevel(20)   #利用handelr对象设置日志等级：设置日志的显示级别，显示当前级别比它高的级别
#创建一个日志格式对象
formatter=logging.Formatter("%(asctime)s_k_%(name)s_%(levelname)s_%(message)s")
#把日志格式对象配置到handler对象        #当前时间    日志名称      日志级别        日志内容
handler1.setFormatter(formatter)

handler2=logging.FileHandler('./test.log','a',encoding='utf-8')
handler2.setLevel(40)
formatter1=logging.Formatter("%(asctime)s_k_%(name)s_%(levelname)s_%(message)s")
handler2.setFormatter(formatter1)

log_obj.addHandler(handler1)    #核心 把handler对象设置加载到日志对象
log_obj.addHandler(handler2)
#formatter-->handler1-->log_obj

#日志的举例：
log_obj.debug('debug')  #10,20,30,40,50
log_obj.info('info')
log_obj.warning('warning')
log_obj.error('error')
log_obj.critical('critical')














