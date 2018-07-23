# -*- coding:utf-8 -*-

import requests,json
from pyecharts import Bar


url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_513791211?csrf_token="
url_1 = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_29800567?csrf_token="
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
headers = {"User-Agent":user_agent}
params = "fr6NiHpeVLr9NtVU8Tp/cERnEAi5AOPK0Toc4Uwl74qL9NDsPqSq18CmMArSTjFkiRdZ1WdQITnqiYAUChOFxeigJPBNUrkOs8agT+AlgG009IpzJv2Jnc6nAD5sRLKwfTxa+3s1vzqyZiCkMDuTFdPuw8s+4AttvMbEFPf7rPMVyCF96s62uEvsmnxenLjq"
params_1 = 'r8nlJz3LzA9E5im8li7Y+OtePZtobExNoUOq9LhwDA1TO1WAfxGqNljCt3ZldAA09tbTY+TpiB59C1w1eOTvl6VgIDQRSEITKEGUqibM0p8oa1Z18lgRu+LW4NVOLEbe'
encseckey = "1cb02ed0c6ac8e13541d62bad526f7f2a6c247a5db4bf7a9b149996d2f7547178d3d81bf5bd8d6f1440ba9f7f60d97f6294b629d579c2e7e790658f3ffca0b75b7ece4eee90deaa189fcc9414900c2a3ad60caf592b9605e10c3dd6765bc0f588a962623679e98b86afc0fdcb3f47a9243706b5946fc7084b11c0bf38a97a015"
encseckey_1 = "03bc71a98a429a590cf10ff373e8ab5ce4a5c70ba25a3aebdf48a810d28a073f373fad06b22695835d502adc937d423f3540dcbcdfa9e22093e74cbbb454a0bf56cc8e27b0a2bb133b5060c5018581021bdf219a3ebe21aad8ec3ecddc695e171fba786fe75d80f0a4a8ef598a393b6b7106ec5876bdf970aa4c48842143f5d6"
form_date = {
    # "params":params,
    # "encSecKey":encseckey
    "params":params_1,
    "encSecKey":encseckey_1
}

response = requests.post(url=url,headers=headers,data=form_date)
response = requests.post(url=url_1,headers=headers,data=form_date)
# print (response.status_code)
# data = json.loads(response.text)
data = response.text
print(data)
# print(type(data))
# for key in data:
#     print(key)
#     print (data[key])
# print(data['hotComments'])
'''
hotComments = []
for value in data['hotComments']:
    data_ = {
        "username":value['user']['nickname'],
        "likecount":value['likedCount'],
        'content':value['content']
    }
    hotComments.append(data_)

# print(hotComments)
content_list = [content['content'] for content in hotComments]
likecount_list = [content['likecount'] for content in hotComments]
username_list = [content['username'] for content in hotComments]

bar = Bar("热评点赞示例图")
bar.add("点赞数量",username_list,likecount_list,is_stack=True,mark_line=["min","max"],mark_point=["average"])
bar.render()
'''
