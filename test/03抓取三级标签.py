# -*- coding:utf-8 -*-
# @Desc: 测试抓取三级标签

import requests
import lxml
from lxml import etree

url = "https://www.biquge5200.cc/3_3153/"

response = requests.get(url).text
# print(response)

mytree = lxml.etree.HTML(response)

level3List = mytree.xpath("//div[@id='list']//dd[position()>9]")
for i in level3List:
    chapter = i.xpath("./a/text()")[0]
    chapterUrl = i.xpath("./a/@href")[0]
    print(chapter, chapterUrl)
