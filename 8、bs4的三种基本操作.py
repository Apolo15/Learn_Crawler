from bs4 import BeautifulSoup

# 定义html文档内容
html_doc = """
<html><head><title abc="123">The Dormouse's story</title></head> 
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>

"""

#创建一个bs对象，这个bs对象需要指定解析器
soup=BeautifulSoup(html_doc,'lxml')

#1、通过tag标签获取文档数据
r=soup.title
r=soup.title['abc'] #获取title标签上abc的值
r=soup.p #多个p只返回第一个
r=soup.p['class']
r=soup.title.text




#2、通过搜索【获取】页面中的【元素】 find（首项） find_all（所有）
r=soup.find('a')
r=soup.find_all('a')
r=soup.find('title')

print(r)
print(r.text)


#3、css选择器
# 通过标签 选择元素
r = soup.select('title')

# 通过class类名获取元素
r = soup.select('.title')

# 通过ID名获取元素
r = soup.select('#link2')

# 通过空格 层级关系获取元素
r = soup.select('html body p')

# 通过逗号，并列关系获取元素
r = soup.select('a,title')