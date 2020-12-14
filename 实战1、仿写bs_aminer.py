#

from bs4 import BeautifulSoup
import requests

#1、定义请求的url和请求头
url='https://gct.aminer.cn/eb/gallery/detail/eb/5d525f7a530c70a9b3631ecf'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
#2、发送请求
res = requests.get(url,headers=headers)


#3、判断是否请求成功，并获取请求的源代码
if res.status_code==200 or 304:
    print(res.text)

    # 4、解析数据
    soup=BeautifulSoup(res.text,'lxml')
    #print(soup)
    #获取页面中所有的作者？模块？ 这个地方的class要加上下划线
    divs=soup.find('div',class_='avatar_zone')
    #print(divs)
    #验证找到数据成功
    #for i in divs:
      #  print(i.find('div',class_="title"))
    # 5、写入数据
