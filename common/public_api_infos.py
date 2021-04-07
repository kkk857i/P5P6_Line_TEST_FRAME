
import json
import jsonpath
from common.config_utils import config
from requests.exceptions import RequestException
from common.log_utils import logger


def get_access_token_api(session,url_params):
    logger.info('************************************')
    logger.info('*执行调用get_access_token_api接口开始*')
    try:
        response = session.get(url= 'https://%s/cgi-bin/token'% config.HOSTS,
                    params=url_params)
    except RequestException as e:
        logger.error('请求出现异常，错位原因是:%s'%e.__str__())
    finally:
        logger.info('*执行调用get_access_token_api接口结束*')
        return response

def get_access_token(session):
    url_params = {
        "grant_type": "client_credential",
        "appid": config.APPID,
        "secret": config.SECRET
    }
    response = get_access_token_api(session,url_params)
    print(response.text,'22')
    token_value = jsonpath.jsonpath(response.json(),'$.access_token')[0]
    print(token_value,'token_value')
    return token_value

def create_user_tag_api(session,url_params,post_data):
    post_data_str = json.dumps(post_data, ensure_ascii=False)
    response = session.post('https://%s/cgi-bin/tags/create' % config.HOSTS,
                                 params=url_params,
                                 data=post_data_str.encode('utf-8'))
    return response

def delete_user_tag_api(session,url_params,post_data):
    response = session.post('https://%s/cgi-bin/tags/delete' % config.HOSTS,
                            params=url_params,
                            json=post_data)
    return response

def get_create_usertag(session,url_params):
    response = session.get('https://%s/cgi-bin/tags/get' % config.HOSTS,
                           params=url_params)
    return response

def update_usertag(session,url_params,post_data):
    # post_data_str = json.dumps(post_data, ensure_ascii=False)
    response = session.post('https://%s/cgi-bin/tags/updata' % config.HOSTS,
                            params=url_params,
                            data=json.dumps(post_data))
    print(response.text,'22')
    return response

def gettag_fans_list(session,url_params,post_data):
    post_data_str = json.dumps(post_data, ensure_ascii=False)
    response = session.post('https://%s/cgi-bin/user/get' % config.HOSTS,
                            params=url_params,
                            data=post_data_str.encode('utf-8'))
    print(response.text, '33')
    return response











