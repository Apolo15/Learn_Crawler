from lxml import etree

html=etree.HTML('./test2.html',etree.HTMLParser())

print(html)

r=html.xpath('/bookstore/book[1]')
print(r)