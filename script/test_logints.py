# 创建测试类
from api.login import LoginAPI


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
    def test01_login_success(self):
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginApi.uuid
        }

        response = self.login_api.login(test_data=login_data)
        # 断言
        assert 200 == response.status_code
        # 断言响应数据包含“成功”
        assert '成功' in response.text
        # 断言响应json数据中code的值
        assert 200 == response.json().get('code')

    # 登录失败（用户名为空）
    def test01_login_failue(self):
        login_data = {
            "username": " ",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginApi.uuid
        }

        response = self.login_api.login(test_data=login_data)
        # 断言
        assert 200 == response.status_code
        # 断言响应数据包含“错误”
        assert '错误' in response.text
        # 断言响应json数据中code的值
        assert 500 == response.json().get('code')

    # 登录失败（用户不存在）
    def test01_login_failue2(self):
        login_data = {
            "username": "gxb",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginApi.uuid
        }

        response = self.login_api.login(test_data=login_data)
        # 断言
        assert 200 == response.status_code
        # 断言响应数据包含“错误”
        assert '错误' in response.text
        # 断言响应json数据中code的值
        assert 500 == response.json().get('code')
