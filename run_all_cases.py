

import unittest
import os
import sys
import shutil
from common import HTMLTestReportCN
from common.log_utils import logger
from common.email_utlis import EmailUtils

current_path=os.path.dirname(__file__)
case_path=os.path.join(current_path,'testcases')
html_repost_path=os.path.join(current_path,'html_reports/')

# print(case_path)
logger.info('**微信接口测试开始执行**')
discover_cases = None
try:
    discover_cases=unittest.defaultTestLoader.discover(start_dir=case_path,
                                                   pattern='tests*.py')
except ImportError as e:
    logger.error('测试用例路径配置出错，不能加载测试用例')
except Exception as e:
    logger.error('系统错误，错误原因:%s'%e.__str__())

api_case_suite=unittest.TestSuite()
if discover_cases:
    api_case_suite.addTest(discover_cases)
    logger.info('加载测试用例到测试套件成功')
else:
    logger.error('加载测试用例到测试套件失败')

# unittest.main(verbosity=2,defaultTest='api_case_suite')

#测试报告路径的对象
html_repost_path_obj=HTMLTestReportCN.ReportDirectory(html_repost_path)
html_repost_path_obj.create_dir('WX_API_TEST_') #创建测试报告文件夹路径
#获取测试报告网页文件的路径
html_report_file_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
html_repost_file_obj = open(html_report_file_path,'wb')   #创建html网页文件
logger.info('创建测试报告路径:%s' % html_report_file_path)
runner=HTMLTestReportCN.HTMLTestRunner(stream=html_repost_file_obj,
                                       tester='k',
                                       title='微信公众号接口测试项目',
                                       description='实战使用')
runner.run(api_case_suite)

email_body='''
<h1 align="center"> 接口自动化测试报告 </h1>
<p align="center"> 详情见附件 </p>
'''
#EmailUtils发送邮件
# EmailUtils(email_body,html_report_file_path).send_email()

#jenkins发邮件--优化前后
#copyfile强制复制不提醒
# shutil.copyfile(html_report_file_path,sys.argv[1])
# shutil.copyfile(html_report_file_path,'%s/WX_API_TEST.html' % sys.argv[1])















































