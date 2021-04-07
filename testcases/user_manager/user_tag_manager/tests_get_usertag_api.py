import unittest
import requests
import jsonpath
from common.config_utils import config
from common import public_api_infos


class TestGetUsertagApi(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.HOSTS
        self.session = requests.session()

    def tearDown(self) -> None:
        self.session.close()

    def test_get_create_usertag(self):
        self._testMethodName = 'api_case_05'
        self._testMethodDoc = '获取已创建的用户标签接口'
        token_id = public_api_infos.get_access_token(self.session)
        url_params = {
            "access_token": token_id
        }
        response = public_api_infos.get_create_usertag(self.session, url_params)
        print(response.text)
        actual_result = jsonpath.jsonpath(response.json(), '$.tags[0].name')[0]
        self.assertEqual(actual_result, "星标组", 'api_case_05用例执行成功')


if __name__ == '__main__':
    unittest.main(verbosity=2)
