
#re.sub函数 用于替换字符床中的匹配项
import re

str1 = '135 7766 8899 , 湖南号码'
str1 = str1.replace(' ','')
print(str1)

str1 = '135  7766 8899 , 湖南号码'
result_01 = re.sub('\d\s+\d','',str1)
print(result_01)

result_02 = re.sub('(\d+)\s+(\d+) (\d+)',r'\1\2\3',str1)    #\1\2表示（）的分组
print(result_02)

# result_03 = re.sub('\s,.*$','',str1)
result_03 = re.sub(r'\s',"", str1)  #替换空格为空
print(result_03)
