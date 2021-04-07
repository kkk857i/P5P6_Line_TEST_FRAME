
#re.split 能够匹配的子串将字符串分割后返回列表
import re

str1 = '中国$韩国$日本$英国'
print(str1.split('$'))

str2 = '中国1韩国2日本3英国'
print(re.split('\d',str2,maxsplit=3))  #maxsplit maxsplit=1 分割一次，默认为0 ，不限制

str3= '中国 韩国  日本  英国  德国'
print(re.split('\s+',str3))













