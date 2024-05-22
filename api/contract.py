#合同上传接口封装

import requests

import config


class ContractApi:
    def __init__(self):
        # self.url_upload = 'http://kdtx-test.itheima.net/api/common/upload'
        self.url_upload = config.BASE_URL + '/api/common/upload'
        # self.add_contract = 'http://kdtx-test.itheima.net/api/contract'
        self.add_contract = config.BASE_URL + '/api/contract'
    # 合同上传接口
    def upload_contract(self, test_data,token):
        return requests.post(url=self.url_upload,files={"file": test_data},headers={"Authorization" : token})

    #合同新增接口
    def put_contract(self,test_data,token):
        return requests.post(url=self.add_contract,json=test_data,headers={"Authorization" : token})