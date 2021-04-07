
# #方法1：
# class ConfigUtils:
#     @property   #方法==变成属性方法
#     def HOSTS(self):
#         return 'api.weixin.qq.com'
#
# config=ConfigUtils()
#
# if __name__=='__main__':
#     print(config.HOSTS)


#方法2：
import configparser
import os

config_file_path = os.path.join(os.path.dirname(__file__),'..','conf','config.ini')

class ConfigUtils :
    def __init__(self, config_file=config_file_path):
        self.cfg_obj = configparser.ConfigParser()
        self.cfg_obj.read(config_file, encoding='utf-8')

    @property
    def HOSTS(self):
        hosts_value = self.cfg_obj.get('default','HOSTS')
        return hosts_value

    @property
    def CASE_PATH(self):
        case_path_value = self.cfg_obj.get('path','CASE_PATH')
        return case_path_value

    @property
    def APPID(self):
        appid_value = self.cfg_obj.get('user_info','APPID')
        return appid_value

    @property
    def SECRET(self):
        secret_value = self.cfg_obj.get('user_info', 'SECRET')
        return secret_value

    @property
    def SMTP_SERVER(self):
        smtp_server_value = self.cfg_obj.get('email', 'SMTP_SERVER')
        return smtp_server_value


config = ConfigUtils()

if __name__ == '__main__':
    print(config.APPID)
    print(config.SMTP_SERVER)



