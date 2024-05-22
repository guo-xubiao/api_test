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

    # 课程修改成功
    def test01_update_success(self):
        update_data = {
            "id": 93,
            "name": "接口测试001",
            "subject": "6",
            "price": 998,
            "applicablePerson": "2",
            "info": "课程介绍001"
        }
        res = self.course_api.update_course(test_data=update_data, token=TestAddCourseAPI.TOKEN)
        print(res.json())
        assert 200 == res.status_code
        assert "成功" in res.text
        assert 200 == res.json().get("code")

    def test02_update_false(self):
        update_data = {
            "id": "",
            "name": "接口测试001",
            "subject": "6",
            "price": 998,
            "applicablePerson": "2",
            "info": "课程介绍001"
        }
        res = self.course_api.update_course(test_data=update_data, token=TestAddCourseAPI.TOKEN)
        print(res.json())
        assert 200 == res.status_code
        assert "失败" in res.text
        assert 500 == res.json().get("code")

    # def test03_update_false(self):
    #     update_data = {
    #         "id": "a",
    #         "name": "接口测试001",
    #         "subject": "6",
    #         "price": 998,
    #         "applicablePerson": "2",
    #         "info": "课程介绍001"
    #     }
    #     res = self.course_api.update_course(test_data=update_data, token=TestAddCourseAPI.TOKEN)
    #     print(res.json())
    #     assert 200 == res.status_code
    #     assert "失败" in res.text
    #     assert 500 == res.json().get("code")

    def test04_update_false(self):
        update_data = {
            "id": 6666666,
            "name": "接口测试001",
            "subject": "6",
            "price": 998,
            "applicablePerson": "2",
            "info": "课程介绍001"
        }
        res = self.course_api.update_course(test_data=update_data, token=TestAddCourseAPI.TOKEN)
        print(res.json())
        assert 200 == res.status_code
        assert "失败" in res.text
        assert 500 == res.json().get("code")

    def test05_update_false(self):
        update_data = {
            "id": 93,
            "name": "接口测试001",
            "subject": "6",
            "price": 998,
            "applicablePerson": "2",
            "info": "课程介绍001"
        }
        res = self.course_api.update_course(test_data=update_data, token="xxx")
        print(res.json())
        assert 200 == res.status_code
        assert "认证失败" in res.text
        assert 401 == res.json().get("code")
