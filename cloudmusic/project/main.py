#! /usr/bin/python3
#coding:utf-8

import requests,json,time,base64
from bs4 import BeautifulSoup
from Crypto.Cipher import AES

url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_29800567?csrf_token="
User_Agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
headers = {"Usser-Agent":user_agent}
headers_ = {
        # Accept: */*
        # Accept-Encoding: gzip, deflate, br
        # Accept-Language: en-US,en;q=0.9
        # Connection: keep-alive
        # Content-Length: 484
        # Content-Type: application/x-www-form-urlencoded
        "Cookie":"_iuqxldmzr_=32; _ntes_nnid=2a1c71e1c29a9873d021333f88f2400f,1532182354926; _ntes_nuid=2a1c71e1c29a9873d021333f88f2400f; WM_TID=0WQeAdUrHS96hc9Y95dMFK944iOf7P0R; JSESSIONID-WYYY=rhZK6os3311jvAtsYpPH%2FizeswTZNXMj3%2Bpg5wY5fykhhdrgrQbdZn4EZtFk7e51WHeicxY3ghOtRUjfsUHN21Ahv%2BbSxN%2Fr2%5CZlhVlfv%5Cln%2BD3wzokOC4TO%5C3dpOAdtsCRfWXro%2BhBcHborjX4xPJr2%2BqndrQDB5zfb1TZhw2fS%2B2K6%3A1532272187334; __utma=94650624.11080218.1532182355.1532185181.1532270388.3; __utmc=94650624; __utmz=94650624.1532270388.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=3R9u%2FKD8CTm8dAPaSRlLNtzMJfdoi2%2FyqakqiOb5yFwLnCgywuHstPJSy5FcbbKN0g6ZSYU8uwHe6QOmvkpN1McJpupGlYc3VP28MK6rhMO9A1jn1XbvjgyJIwsW0%2B%2FSWEs%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eedad834fbf5c0b4ef7aa5e7bed2eb3f988c97bbce5eb4ee96a8f834bc88ff96dc2af0fea7c3b92af18ef796ae4188e88db5f034a89fa082d25ab0948295f9478abaac90ec3aeda7bf82ea7bab91aed6fc4eb594a2a4e673b5ab8894f75c8a8db7d6c569a2be85afb36df6869dbad834b7a98886b55b8db3ba8cf346f393adabf37fb499a4bae2399690fed9d041f6aea8aece3383efa68fb454a2aaa688fc428ba9bdb8b321ed8d99a6f237e2a3; playerid=55127037; __utmb=94650624.5.10.1532270388",
        # Host: music.163.com
        # Origin: https://music.163.com
        # Referer: https://music.163.com/song?id=29800567
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

#first_param = "{rid:'', offset:'0', total:'true' limit:'20', csrf_token:''}"
second_param = "010001"
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_param = "0CoJUm6Qyw8W8jud"

def get_encsekey():
    encsekey = "03bc71a98a429a590cf10ff373e8ab5ce4a5c70ba25a3aebdf48a810d28a073f373fad06b22695835d502adc937d423f3540dcbcdfa9e22093e74cbbb454a0bf56cc8e27b0a2bb133b5060c5018581021bdf219a3ebe21aad8ec3ecddc695e171fba786fe75d80f0a4a8ef598a393b6b7106ec5876bdf970aa4c48842143f5d6"
    return encsekey

def get_params(page):  # page为传入页数
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'y'
    if (page == 1):  # 如果为第一页
        first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
        h_encText = AES_encrypt(first_param, first_key, iv)
    else:
        offset = str((page - 1) * 20)
        first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' % (offset, 'false')
        h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)
    return h_encText

def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    # print (type(text))
    if isinstance(text,bytes):
        text = text.decode() + pad * chr(pad)
    else:
        text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text

def get_json(url, params, encSecKey):
    print(params)
    print(encSecKey)
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers_, data=data)
    print (response.status_code)
    print (response.text)
    return response.content


if __name__ == "__main__":
    p1 = "9yVmjygk/5kyK2A42f7kXpOr69vEnIIlEAGCGy2g17O627B9OOUzvBXsgWrlFjEpl+GVJ5GZd7MPoF8mGNpiVU4JHxjdp0Us0c3GI6sB8kGuwf3xniTfe2iXHiGITWfS/QakbS67AwVuMFuraGP4MTToodYa/7M+hVajci2WyWFXs1PNcgcG3LkM3qDwpByH"
    k1 = "2f6f182a36dd17a53c78543191224cea3f934a4eb093a4ba176a9244e1146e77d7c184c5b7e3790ea3fcd7eb5fc553f556b43a318fc6ce674e1499a0335c77b000294fcf0a83354419e47f40a642d1e4a44972527b4ddfd6a3edc9e8b643d4f7c2015146d643571c7d4174ec36a8a0ff46901f0429a5b56c40683ee5262dd9bd"
    p2 = "QonSp3xzNpCVxUSmIdV3GSB9Ef4Zvac0u1OhVou1lsoF5+S45UuuMlvJKJLCrfBrzVS+1MUjnwmkxGuI1DaZHNrbhgWRbXNHKbXMD05qkFaQDBU4eui/Zqy1fhHjZJhgnwbi5LddVdzVYJMih6NkjzYPdMWjbBAkTszU90mypN4UholsdZCN8NlSojX0AIBq"
    k2 = "bbb3e204ca4a2c4b9a0726e9c65b4c9255b0bfb568d2028f843556ad02aed22c6fae01dbd92cf6286c411e5c62abc01abc0642451b43c90057eee5a69eb409b3db7daee8b0a4738f490634649e9d401271826a24a0c2fcb1d36474e1b5d40a1d39a10e63cef9a0302672e079786636edb466ae140056f4eef9330a2af8aa24ed"


    # print("here")
    # print(get_params((2)))
    # print(get_encsekey())
    content = get_json(url,get_params(1),get_encsekey())
    # content = get_json(url, p2,k2)
    # print (content.text())

