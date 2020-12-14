import requests

#定义请求的url
url='http://www.baidu.com'
#发起get请求
res=requests.get(url)

#获取相应结果
print(res)   #这是个response对象  <Response [200]>
print(res.content)#b'....'  这是个二进制数据流
print(res.content.decode('utf-8'))#decode：解码   把二进制文本按照utf-8的字符集转化为普通字符串
#print(res.text)    这个等同于utf-8.都是获取响应的内容
print(res.headers)  #请求的头信息
print(res.status_code) #请求的状态码，200表示正常 404就是找不到还有500服务器内部问题什么的