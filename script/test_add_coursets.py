# 导包
import json
import pymysql
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

    # 后置处理
    # 课程添加成功
    def test01_success(self):
        # 准备测试数据
        add_data = {
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
        }
        # 调用接口
        res = self.course_api.add_course(test_data=add_data, token=TestAddCourseAPI.TOKEN)
        result = json.loads(res.text)
        print(result)
        # 断言响应状态码
        assert 200 == res.status_code
        # 断言返回数据中包含指定的文字
        assert "成功" in res.text
        # 断言json返回数据code值
        assert 200 == res.json().get("code")
    # # 程添加失败(未登录)
