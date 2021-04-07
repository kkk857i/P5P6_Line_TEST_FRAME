
#findall() 查找所有
import re

str1 = 'hello 123 hello'
result_01 = re.search('\w+',str1)
result_02 = re.findall('\w+',str1)

pattern_01 = re.compile('\w+')
#函数语法，
result_03 = pattern_01.findall(str1,pos=5,endpos=13)

print(result_01)
print(result_02)
print(type(result_03))

