
import os
import smtplib
from email.mime.text import MIMEText    #导入email文本样式
from email.mime.multipart import MIMEMultipart  #导入文件模块

email_body='''
<h1 align="center">接口自动化测试报告</h1>
<p align="center">详情见附件</p>
'''

html_file_path = os.path.join(os.path.dirname(__file__),'..',
                              'html_reports','Wx_API_TEST_V1.8','WX_API_TEST_V1.8.html')

text_obj = MIMEText(email_body,'html','utf-8')  #创建一个正文的对象

attach_file = MIMEText( open (html_file_path,'rb').read(),'base64','utf-8')
attach_file['Content-type'] = 'application/octet-stream'
attach_file.add_header('Content-Disposition','attachment',
                       filename=('gbk','','WX_API_TEST_V1.8.html'))   #有中文写法
# attach_file['Content-Disposition'] = 'attachment;filename="WX_API_TEST_V1.8.html"'     #无中文写法

email_obj = MIMEMultipart()   #创建一个文件对象
email_obj.attach( text_obj )    #增加一个文本格式正文
email_obj.attach(attach_file)
email_obj['from'] = '1067270040@qq.com'   #发件人
email_obj['to'] = '1067270040@qq.com' #收件人
email_obj['Cc'] = '1004926490@qq.com,1421899585@qq.com'    #抄送人
email_obj['subject'] = '接口自动化测试报告'

smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com")
#邮箱授权码：
smtp.login(user='1067270040@qq.com',password='yncyyagtvudubcah')
smtp.sendmail('1067270040@qq.com','1067270040@qq.com',email_obj.as_string())
# smtp.sendmail('1067270040@qq.com',['1067270040@qq.com','1004926490@qq.com'],email_obj.as_string())

smtp.close()




















