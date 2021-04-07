


#正则表达式基础

import re

str1 ='newdream'
str2 ='''
hllo123he
hello123kkh
123hello
hello123hao
'''

#方式一：
pattern_01 = re.compile('n\w+m')
result_01 = re.match(pattern_01,str1)
print(result_01.group())

pattern_02 = re.compile('123\w+o')
result_02 = re.findall(pattern_02,str2)
print(result_02)

#方式2
result_03 = re.match('n\w+m',str1)
print(result_03.group())

#方式3：
result_04 = pattern_01.match(str1)
print(result_04.group())