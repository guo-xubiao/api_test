import  requests
import config
#创建接口类
class LoginAPI:
    def __init__(self):
        # self.url_verify = 'http://kdtx-test.itheima.net/api/captchaImage'
        self.url_verify = config.BASE_URL + "/api/captchaImage"
        # self.url_login = "http://kdtx-test.itheima.net/api/login"
        self.url_login = config.BASE_URL + "/api/login"

    #验证码
    def get_verify_code(self):
        return requests.get(self.url_verify)


    #登录
    def login(self,test_data):
        return requests.post(url=self.url_login,json=test_data)