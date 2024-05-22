import config
from api.contract import ContractApi
from api.login import LoginAPI
from api.course import CourseApi


# 创建测试类
class TestContractBusiness:
    # 前置处理
    def setup_method(self):
        # 实例化接口对象
        self.login_api = LoginAPI()
        self.course_api = CourseApi()
        self.contract_api = ContractApi()

    def teardown_method(self):
        pass

    # 1.登陆成功
    def test01_login_success(self):
        # 获取验证码
        res_v = self.login_api.get_verify_code()
        print(res_v.status_code)
        print(res_v.json())
        print(res_v.json().get('uuid'))

        # 登录
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": res_v.json().get('uuid')
        }
        res_l = self.login_api.login(test_data=login_data)
        print(res_l.status_code)
        print(res_l.json())
        # 提取登录成功之后的token数据并保存在类的属性中
        TestContractBusiness.token = res_l.json().get('token')
        print(TestContractBusiness.token)

    # 2.新增课程
    def test02_add_course(self):
        add_data = {"name": "测试开发提升课01",
                    "subject": "6",
                    "price": 899,
                    "applicablePerson": "2",
                    "info": "测试开发提升课01"}
        response = self.course_api.add_course(test_data=add_data, token=TestContractBusiness.token)
        print(response.json())

    # 3.上传合同
    def test03_upload_contract(self):
        # 读取pdf文件数据
        f = open(config.BASE_PATH + "/data/test.pdf", "rb")
        response = self.contract_api.upload_contract(test_data=f, token=TestContractBusiness.token)
        print(response.json())

    # 4.新增合同
    def test04_add_contract(self):
        add_data = {"name": "测试888",
                    "phone": "13612341888",
                    "contractNo": "HT10012004",
                    "subject": "6",
                    "courseId": 99,
                    "channel": "0",
                    "activityId": 77,
                    "fileName": "/profile/upload/2023/01/05/86e5a3b8-b08c-470c-a17d-71375c3a8b9f.pdf"
                    }
        response = self.contract_api.put_contract(test_data=add_data,token=TestContractBusiness.token)
        print(response.json())
