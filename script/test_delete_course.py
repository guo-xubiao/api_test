# 导包
import pytest
from api.login import LoginAPI
from api.course import CourseApi
# 创建测试类
class TestAddCourseAPI:
    TOKEN = None
    #前置处理
    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseApi()

        res_v = self.login_api.get_verify_code()

        login_data={
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": res_v.json().get("uuid")
        }

        res_l = self.login_api.login(test_data=login_data)

        TestAddCourseAPI.TOKEN = res_l.json().get("token")
        print(TestAddCourseAPI.TOKEN)

    def test01_delete_success(self):
        res = self.course_api.delete_course(test_id=3,token=TestAddCourseAPI.TOKEN)
        print(res.json())
        assert 200 == res.status_code
        assert "成功" in res.text
        assert 200 == res.json().get("code")

    def test02_delete_false(self):
        res = self.course_api.delete_course(test_id=666666,token=TestAddCourseAPI.TOKEN)
        print(res.json())
        print(res.status_code)
        assert 200 == res.status_code
        assert '失败' in res.text
        print(res.json().get("code"))
        assert 500 == res.json().get("code")

    def test03_delete_false(self):
        res = self.course_api.delete_course(test_id=110,token="xxx")
        print(res.json())
        assert 200 == res.status_code
        assert '认证失败' in res.text
        assert 401 == res.json().get("code")