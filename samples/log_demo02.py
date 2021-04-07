

import logging

#相当于输出语句，默认输出eroor级别，info是不能输出的
#
# logging.info('info')
# logging.error('eroor')

log_obj = logging.getLogger('cs')
log_obj.setLevel(10)
handler1 = logging.StreamHandler()  #创建一个handler对象，输出到控制台
handler1.setLevel(20)
formatter = logging.Formatter("%(asctime)s_k_%(name)s__%(levelname)s__%(message)s")

handler1.setFormatter(formatter)

handler2 = logging.FileHandler('./test.log','a',encoding='utf-8')
handler2.setLevel(40)
formatter1=logging.Formatter("%(asctime)s_k_%(name)s__%(levelname)s__%(message)s")
handler2.setFormatter(formatter1)

log_obj.addHandler(handler1)
log_obj.addHandler(handler2)

log_obj.debug('debug')  #10,20,30,40,50
log_obj.info('info')
log_obj.warning('warning')
log_obj.error('error')
log_obj.critical('critical')














