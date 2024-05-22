import requests

response = requests.get("http://kdtx-test.itheima.net/api/captchaImage" )

print(response.status_code)
print(response.text)
