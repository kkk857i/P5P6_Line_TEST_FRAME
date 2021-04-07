

import unittest
import requests
import jsonpath
from common.config_utils import config
from common import public_api_infos


class TestUpdateUserTag(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.HOSTS
        self.session = requests.session()

    def tearDown(self) -> None:
        self.session.close()

    def test_update_usertag(self):
        self._testMethodName = 'api_case_06'
        self._testMethodDoc = '更新用户标签接口'
        token_id = public_api_infos.get_access_token(self.session)

        url_params ={
            "session_token": token_id
        }
        post_data_json = {"tag": {"id": 100,     "name": "13366"}}

        response = public_api_infos.update_usertag(self.session, url_params, post_data_json)
        actual_result = jsonpath.jsonpath(response.json(), '$.errcode')[0]
        self.assertEqual(actual_result, 0, 'api_case_06用例执行结束')

if __name__ == '__main__':
    unittest.main(verbosity=2)






