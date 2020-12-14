import requests

#操作时的地址
url='https://www.lmonkey.com/login'

url1='https://www.lmonkey.com/my/order'
#操作之后的目标的请求地址，在response里找

#session 我的理解为高级的request的对象，他带有记录cookie 的功能
#普通的request不带这个功能
session =requests.session()


headers={
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36'

}

data={
    '_token': 'ljckJiGc4aGAOUupefE0mFdaMQr7aNIzj8y19aSL',
    'username': 'ax445534736',
    'password':'milk2580'
}

#只有在post方法的时候才会有form data 的数据。

res=session.post(url=url,headers=headers,data=data)

if res.status_code==200:

    rep=session.get(url1,headers)
    if rep.status_code==200:
        print ("成功了")

else:
    print(res.status_code)



