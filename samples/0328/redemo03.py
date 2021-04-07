
#search 函数 全字符串查找 找到第一个就停止
import re

str1 = 'nE wDreamEwaaa'
# pathher_01 = re.compile('e\w',re.IGNORECASE)
# result_01 = re.search(pathher_01, str1)
result_01 = re.search('e\w' ,str1 ,re.I)
print(result_01.group())

