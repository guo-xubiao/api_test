#课程模块接口封装

import requests
import config
class CourseApi:
    def __init__(self):
        # self.url_add_course = 'http://kdtx-test.itheima.net/api/clues/course'
        self.url_add_course = config.BASE_URL + '/api/clues/course'
        # self.url_select_course = 'http://kdtx-test.itheima.net/api/clues/course/list'
        self.url_select_course = config.BASE_URL + '/api/clues/course/list'
        # self.url_update_course = 'http://kdtx-test.itheima.net/api/clues/course'
        self.url_update_course = config.BASE_URL + '/api/clues/course'
        # self.url_delete_course = 'http://kdtx-test.itheima.net/api/clues/course'
        self.url_delete_course = config.BASE_URL + '/api/clues/course'

    def add_course(self, test_data,token):
        return requests.post(url=self.url_add_course,json=test_data,headers={"Authorization" : token})

    def select_course(self,test_data,token):
        return requests.get(url=self.url_select_course+f"/{test_data}",headers={"Authorization" : token})

    def update_course(self,test_data,token):
        return requests.put(url=self.url_update_course,json=test_data,headers={"Authorization" : token})

    def delete_course(self,test_id,token):
        return requests.delete(url=self.url_delete_course+f"/{test_id}",headers={"Authorization" : token})