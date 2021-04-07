
#finditer() 查找所有 并返回迭代器，迭代器中都是match对象
import re

str1 = 'hello 123 hello'

pattern_01 = re.compile('\w+')
#函数语法，
result_03 = pattern_01.finditer(str1,pos=5,endpos=12)

# print(result_01)
# print(result_02)
print(type(result_03))  #返回一个迭代器，都是match

for r in result_03:
    print(r.group())
