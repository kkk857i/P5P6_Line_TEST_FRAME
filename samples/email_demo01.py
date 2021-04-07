
import smtplib
from email.mime.text import MIMEText    #导入email文本样式

#普通的网页正文文本
email_body='''  
<h1 align="center">接口自动化测试报告</h1>
<p align="center">详情见附件</p>
'''

email_obj = MIMEText(email_body,'html','utf-8') #邮件正文
email_obj['from'] = '1067270040@qq.com'   #发件人
email_obj['to'] = '1067270040@qq.com' #收件人
# email_obj['Cc'] = '1421899585@qq.com'
email_obj['Cc'] = '1004926490@qq.com,1421899585@qq.com'    #抄送人
email_obj['subject'] = '接口自动化测试报告'

smtp = smtplib.SMTP()   #创建邮件发送对象
smtp.connect("smtp.qq.com")     #邮箱的主机地址
#登陆邮箱授权码：
smtp.login(user='1067270040@qq.com',password='yncyyagtvudubcah')
smtp.sendmail("1067270040@qq.com",'1067270040@qq.com',email_obj.as_string())    #转成str格式发送

smtp.sendmail('1067270040@qq.com',['1067270040@qq.com','1421899585@qq.com'],email_obj.as_string())

smtp.close()




















