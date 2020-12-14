#res=request.post(url,header,[post]的参数）


import requests
import json

#这个url 可以去network 里面的【XHR】分组里找 XHR：xmlhttprequest
url='https://fanyi.baidu.com/sug'

headers={
    'user-agent':'user-agent: Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
}

data={
    'kw':'你好'
}

res=requests.post(url,headers=headers,data=data)
resp=json.loads(res.text)

code=res.status_code
print(code)
print(res.text)
print(resp)