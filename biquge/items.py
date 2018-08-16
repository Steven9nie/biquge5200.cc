# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):

    level1 = scrapy.Field()  # 一级标签
    level2 = scrapy.Field()  # 二级标签
    author = scrapy.Field()  # 作者
    chapter = scrapy.Field()  # 三级标签,章节
    title = scrapy.Field()  # 标题
    content = scrapy.Field()  # 正文
