
import unittest
import requests
import jsonpath
from common.config_utils import config
from common import public_api_infos

class GettagFansListApi(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.HOSTS
        self.session = requests.session()

    def tearDown(self) -> None:
        self.session.close()

    def test_gettag_fans_list(self):
        self._testMethodName = 'api_case_07'
        self._testMethodDoc = '获取标签下粉丝列表接口'
        token_id = public_api_infos.get_access_token(self.session)
        url_params = {
            "access_token": token_id
        }
        post_data_json = {"tagid": 9990,   "next_openid": ""}

        response = public_api_infos.gettag_fans_list(self.session, url_params, post_data_json)
        actual_result = jsonpath.jsonpath(response.json(), '$.next_openid')[0]
        self.assertEqual(actual_result, "ojxbq6qbXhwaqnYj2L-DJJLXU4eU",'api_case_07用例执行成功')

if __name__ == '__main__':
    unittest.main(verbosity=2)










