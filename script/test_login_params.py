# 创建测试类
import config
from api.login import LoginAPI
import pytest
import json
# # 测试数据
# test_data = [
#     ("admin", "HM_2023_test", 200, '成功', 200),
#     ("", "HM_2023_test", 200, '错误', 500),
#     ("gxb", "HM_2023_test", 200, '错误', 500)
# ]

#读取json
def biuld_data(json_file):
    #定义空列表
    test_data =[]
    #打开json文件
    with open(json_file,"r",encoding='utf-8')as f:
        #加载json文件数据
        json_data = json.load(f)
        #便利数据
        for case_data in json_data:
            #转换数据格式[{},{}] ==> [(),()]
            username = case_data.get("username")
            password = case_data.get("password")
            status = case_data.get("status")
            success = case_data.get("message")
            code = case_data.get("code")
            test_data.append((username,password,status,success,code))

    return test_data

class TestLoginApi:
    uuid = None

    # 前置处理
    def setup_method(self):
        self.login_api = LoginAPI()
        # 获取验证码
        response = self.login_api.get_verify_code()
        print(response.json())
        # 提取验证码接口返回uuid
        TestLoginApi.uuid = response.json().get("uuid")
        print(TestLoginApi.uuid)

    # 后置处理
    def teandown_method(self):
        print("结束测试")

    # 登录成功
    @pytest.mark.parametrize("username, password, status, message, code", biuld_data(json_file =config.BASE_PATH + "/data/login.json"))
    def test01_login_success(self,username, password, status, message, code):
        login_data = {
            "username": username,
            "password": password,
            "code": "2",
            "uuid": TestLoginApi.uuid
        }

        response = self.login_api.login(test_data=login_data)
        # 断言
        assert status == response.status_code
        # 断言响应数据包含“成功”
        assert message in response.text
        # 断言响应json数据中code的值
        assert code == response.json().get('code')

