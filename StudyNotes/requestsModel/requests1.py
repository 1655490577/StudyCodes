import requests

req = requests.get('http://www.baidu.com')
# print(req.status_code)  # 状态码
# print(req.encoding)  # 响应的编码方式
# print(req.text)  # 响应的正文信息body
print(req.content.decode('utf-8'))  # 二进制的响应正文信息body
# print(req.cookies)  # 用户cookie信息
# print(req.headers)  # 响应的响应头信息
# print(req.url)  # 响应的url信息

