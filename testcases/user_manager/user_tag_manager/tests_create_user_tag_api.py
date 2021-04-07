
import unittest
import requests
import jsonpath
import json
from common.config_utils import config
from common import public_api_infos

class TestCreateTagApi(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.HOSTS
        self.session = requests.session()
    def tearDown(self) -> None:
        self.session.close()

    def test_01_create_user_tag(self):
        self._testMethodName = 'api_case_03'
        self._testMethodDoc = '验证调用创建标签接口,标签名参数已存在的标签名能否正常处理'
        token_id = public_api_infos.get_access_token(self.session)
        url_params = {
            "access_token": token_id
        }

        post_data_json = {"tag": {"name": "湖南长沙"}}
        response = public_api_infos.create_user_tag_api(self.session,url_params,post_data_json)
        print(response.json())
        actual_result = jsonpath.jsonpath(response.json(),'$.errcode')[0]   #返回数组取值'$.tag.name'
        self.assertTrue(actual_result,45157)

if __name__=='__main__':
    unittest.main(verbosity=2)