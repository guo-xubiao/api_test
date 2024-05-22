# 导包
import pytest
from api.login import LoginAPI
from api.course import CourseApi


# 创建测试类
class TestAddCourseAPI:
    TOKEN = None

    # 前置处理
    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseApi()

        res_v = self.login_api.get_verify_code()

        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": res_v.json().get("uuid")
        }

        res_l = self.login_api.login(test_data=login_data)

        TestAddCourseAPI.TOKEN = res_l.json().get("token")
        print(TestAddCourseAPI.TOKEN)

    # 查询存在的课程
    def test01_select_success(self):
        res = self.course_api.select_course(test_data="?name=测试开发提升课01", token=TestAddCourseAPI.TOKEN)
        print(res.json())
        assert 200 == res.status_code
        assert "成功" in res.text
        assert 200 == res.json().get("code")

    # 查询失败(用户未登录)
    def test02_select_success(self):
        res = self.course_api.select_course(test_data="?subject=6", token="xxx")
        print(res.json())
        assert 200 == res.status_code
        assert "认证失败" in res.text
        assert 401 == res.json().get("code")
