# -*- coding:utf-8 -*-
# @Desc: 测试抓取小说正文

import requests
import lxml
from lxml import etree

url = "https://www.biquge5200.cc/3_3153/143060896.html"

response = requests.get(url).text
# print(response)

mytree = lxml.etree.HTML(response)

title = mytree.xpath("//div[@class=\"bookname\"]/h1/text()")

contentList = mytree.xpath("//div[@id=\"content\"]//text()")
print(title)
# print(contentList)
content = ""
for i in contentList:
    content += i.replace("\u3000", '').replace('\r\n', '').replace('\t', '') + '\n'
print(content)
