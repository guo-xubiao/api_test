import requests

url = "http://kdtx-test.itheima.net/api/login"
header_data = {
    "Content-Type": "application/json"
}
data = {
    "username": "admin",
    "password": "HM_2023_test",
    "code": "2",
    "uuid": "637f479802344788b5041553ae289560"

}

response = requests.post(url=url,headers=header_data, json=data)

print(response.json())