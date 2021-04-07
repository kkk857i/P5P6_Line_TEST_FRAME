

#sub返回一个字符串
#subn返回一个元组

import re

str1 = '''newderam come no!!
google come no!!'''
value = re.subn('(\w+) (\w+) (\w+)',r'\2 \3 \1',str1)   #r 表示原字符集，不会被转码
print(type(value))
print(value)









