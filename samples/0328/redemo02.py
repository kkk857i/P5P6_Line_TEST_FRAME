


#正则表达式基础

import re

# str1 ='1hello123hello'
# str2 ='''hello123hello
# hello1hello
# '''

#方式一：
# result = re.match('\shello[\d,\D]+o',str2)
# print(result.group())
#
# str3 = ''''newdream come on!'
# newdream very good!
# '''
# # # result02 = re.match('.+ .+ .+', str3)
# # result02 = re.match('(.+) (.+) (.+)!', str3)
# # print(result02.group(1,3))
#
# result02 = re.match('(.+)\sCOme(.+)!\s',str3,re.I)
# print(result02)

str1 ='1hello123hello'
str2 ='''
hello123hello
hello1hello
'''

# result = re.match('\d+hello',str1)  #match匹配开头
result = re.match('\shello[\d,\D]+o',str2)
print(result.group())

str3 = '''newdream come on!
newdream very good!
'''
# result_02 = re.match('.+ .+ .+', str3) #（.+？）
# result_02 = re.match('(.+) (.+) (.+)!',str3)
# print(result_02.group(3))
# print(result_02.group(1))
# print(result_02.group(3,1))

result_02 = re.match('(.+)\sCOme (.+)!\s', str3, re.I)  #re.I标志位
print(result_02)








