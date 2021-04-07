#encoding:utf-8

import re
import requests

url_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

response = requests.get(url='https://www.baidu.com/s?wd=云班课',
                        headers=url_headers)

#"title":"云班课 - 用户登录","url":"http://www.baidu.com/link

# print(response.text)
body_str = response.text
titls = re.findall('"title":"(.+?)","url"', body_str)
# print(type(titls)
print(titls)

contens = re.findall('opr-toplist1-subtitle">\s+(.+?)\s+</a>[\s\S]+?([4-9][0-9][0-9]万?)</td>', body_str)
print(contens)



