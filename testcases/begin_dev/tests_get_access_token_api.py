


import unittest
import requests
import jsonpath
from common.log_utils import logger
from common.config_utils import config
from common import public_api_infos


class TestGetAccessTokenApi(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.HOSTS
        self.session = requests.session()

    def tearDown(self) -> None:
        self.session.close()

    def test_01_get_access_token(self):
        '''[api_case_01]验证获取token接口能否正常调用'''
        logger.info('*                                  *')
        logger.info('*      用例[api_case_01]开始执行     *')
        try:
            url_params={
                "grant_type": "client_credential",
                "appid": "wx15938bc8b042cee0",
                "secret": "f01c3e1836d6b40fb24db5dbc0142253"
            }
            response = public_api_infos.get_access_token_api(self.session,url_params)
            json_body = response.json()
            actual_result=jsonpath.jsonpath(json_body,'$.access_token')[0]
            self.assertTrue(actual_result)
        except AssertionError as e:
            logger.info('*      用例[api_case_01]断言失败     *')
        except Exception as e:
            logger.error('%s'%e.__str__())
        finally:
            logger.info('*                                  *')
            logger.info('*      用例[api_case_01]执行结束     *')

    def test_02_grant_type_none(self):
        self._testMethodName = 'api_case_02'
        self._testMethodDoc = '验证grant_type为空时，获取token接口是否能正常处理'
        url_params = {
                "grant_type": "",
                "appid": "wx15938bc8b042cee0",
                "secret": "f01c3e1836d6b40fb24db5dbc0142253"
            }
        response = public_api_infos.get_access_token_api(self.session,url_params)
        json_body = response.json()
        actual_result = jsonpath.jsonpath(json_body,'$.errcode')[0]
        self.assertTrue(actual_result,40002)

if __name__=='__main__':
    unittest.main(verbosity=2)


