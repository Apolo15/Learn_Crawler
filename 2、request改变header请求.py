import requests

url='http://www.xicidaili.com/nn'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}

res=requests.get(url,headers=headers);

code=res.status_code;
print(code)

if code==200:
    with open('./test.html','w') as fp:
        fp.write(res.text)