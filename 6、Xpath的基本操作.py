from lxml import etree

text='''
<html>
  
  <body>
    <div>
      <ul>
        <li class="item-0">
          <a href="link1.html">first item</a></li>
        <li class="item-1">
          <a href="link2.html">second item</a></li>
        <li class="item-inactive">
          <a href="link3.html">third item</a></li>
        <li class="item-1">
          <a href="link4.html">fourth item</a></li>
        <li class="item-0">
          <a href="link5.html">fifth item</a></li>
      </ul>
    </div>
  </body>

</html>
'''
#href 表述的是url，超链接

html=etree.HTML(text)

#这就是全读出来
a=html.xpath('/html/body/div/ul/li/a/text()')
print(a)
#['first item', 'second item', 'third item', 'fourth item', 'fifth item']


#这个是只读一个数组，开始的下标是1不是0
a=html.xpath('/html/body/div/ul/li[1]/a/text()')
print(a)
#['first item']

###=======================================================================
###以上是在一个py文件里进行读取文本
###还可以直接去问价里读,读取一个文件并且解析，解析结果放在html这个对象里，再通过Xpath提取数据
html=etree.parse('./test.html',etree.HTMLParser())

r=html.xpath('/html/body/div/ul/li[1]/a/text()')
print(r)