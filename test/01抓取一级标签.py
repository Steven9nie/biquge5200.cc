# -*- coding:utf-8 -*-
# @Desc: 测试抓取一级标签

import requests
import lxml
from lxml import etree

url = "https://www.biquge5200.cc/"

response = requests.get(url).text
# print(response)

mytree = lxml.etree.HTML(response)

level1List = mytree.xpath('//div[@class=\'nav\']/ul/li[position()>2]')
for i in level1List:
    level1 = "http://" + i.xpath("./a/@href")[0][2:]
    level1Url = i.xpath("./a/text()")[0]
    print(level1, level1Url)
